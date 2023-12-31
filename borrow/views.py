from rest_framework import generics
from rest_framework.views import Response, status
from .models import Borrow
from .serializers import BorrowSerializer, BorrowDetailsSerializer
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from app_copy.permissions import AssociateOnlyPermission
from users.models import User
from app_copy.models import Copy
from drf_spectacular.utils import extend_schema


class BorrowBooksView(generics.ListAPIView):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer

    @extend_schema(
        operation_id="borrow_get",
        description="Mostrar todos os emprestimos de livros",
        tags=["Borrow"],
    )
    def get_queryset(self):
        is_returned = self.request.query_params.get("is_returned")

        queryset = super().get_queryset()

        if is_returned:
            if is_returned.lower() == "true":
                queryset = queryset.filter(is_returned=True)
                return queryset
            elif is_returned.lower() == "false":
                queryset = queryset.filter(is_returned=False)
                return queryset

        return queryset


class BorrowingBookView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AssociateOnlyPermission]

    queryset = Borrow.objects.filter(is_returned=False)
    serializer_class = BorrowSerializer

    @extend_schema(
        operation_id="borrow_post",
        description="Criar emprestimo de livro",
        tags=["Borrow"],
    )
    def perform_create(self, serializer):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        borrows = Borrow.objects.filter(user=user)
        serializerr = BorrowSerializer(borrows, many=True)

        for a in serializerr.data:
            if a["is_active"] == False:
                user.blocked = True
                user.save()
                break
            else:
                user.blocked = False
                user.save()

        book_copy = get_object_or_404(Copy, id=self.kwargs.get("pk"))

        if user.blocked:
            return Response(
                {"detail": "User is blocked!"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if book_copy.quantity == 0:
            return Response(
                {"detail": "Book not avaiable."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer.save(user=user, copy=book_copy)


class BorrowingBookDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AssociateOnlyPermission]

    queryset = Borrow.objects.all()
    serializer_class = BorrowDetailsSerializer
    lookup_url_kwarg = "pk"

    @extend_schema(
        operation_id="borrow_delete",
        description="Soft delete do emprestimo de livro",
        tags=["Borrow"],
    )
    def perform_destroy(self, instance):
        copy_table = Copy.objects.get(id=instance.copy_id)

        copy_table.quantity += 1
        copy_table.save()

        instance.is_returned = True
        instance.save()
