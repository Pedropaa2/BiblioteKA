from rest_framework import generics
from .models import Borrow
from .serializers import BorrowSerializer, BorrowDetailsSerializer
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from users.models import User
from app_copy.models import Copy


class BorrowBooksView(generics.ListAPIView):
    queryset = Borrow.objects.filter(is_returned=False)
    serializer_class = BorrowSerializer


class BorrowingBookView(generics.ListCreateAPIView):
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

    def perform_destroy(self, instance):
        if instance.is_retuned:

            instance.copy.quantity += 1
            instance.copy.save()

            instance.copy.is_retuned = True
            instance.copy.save()

            instance.is_retuned = True
            instance.save()
