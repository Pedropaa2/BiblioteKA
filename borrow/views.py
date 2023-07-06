from rest_framework import generics
from .models import Borrow
from .serializers import BorrowSerializer, BorrowDetailsSerializer
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from users.models import User
from app_copy.models import Copy
from app_copy.serializers import CopySerializer


class BorrowBooksView(generics.ListAPIView):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer

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
    permission_classes = [IsAuthenticated]

    queryset = Borrow.objects.filter(is_returned=False)
    serializer_class = BorrowSerializer

    def perform_create(self, serializer):

        user = get_object_or_404(User, username=self.kwargs.get("username"))
        book_copy = get_object_or_404(Copy, id=self.kwargs.get("pk"))

        if user.blocked:
            raise Exception("Bloceked User!")

        if book_copy.quantity == 0:
            raise Exception("Book not avaible")

        serializer.save(user=user, copy=book_copy)


class BorrowingBookDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Borrow.objects.all()
    serializer_class = BorrowDetailsSerializer
    lookup_url_kwarg = "pk"

    def perform_destroy(self, instance):
        copy_table = Copy.objects.get(id=instance.copy_id)

        copy_table.quantity += 1
        copy_table.save()

        instance.is_returned = True
        instance.save()
