from rest_framework import generics
from rest_framework.views import Response, status
from app_copy.permissions import AssociateOnlyPermission
from .models import Book
from .serializers import BookSerializer, UserBooksSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Book, UserBooks
from django.core.mail import send_mail
import os
import dotenv

class BookListCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AssociateOnlyPermission]
    queryset = Book.objects.all()

    serializer_class = BookSerializer


class FollowBookView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AssociateOnlyPermission]
    queryset = UserBooks.objects.all()
    serializer_class = UserBooksSerializer

    def perform_create(self, serializer):
        pk = self.kwargs["pk"]
        book = Book.objects.get(id=pk)

        serializer.save(follow=self.request.user, book=book)

    def create(self, request, *args, **kwargs):
        book_id = self.kwargs["pk"]

        user = self.request.user

        if UserBooks.objects.filter(follow=user, book_id=book_id).exists():
            return Response(
                {"detail": "You are already following this book."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        response = super().create(request, *args, **kwargs)
        users_following = UserBooks.objects.filter(book_id=book_id).values_list(
            "follow__username", flat=True
        )
        response.data["users_following"] = list(users_following)

        book = Book.objects.get(id=book_id)
        subject = "Novo seguidor de livro"
        message = f"Você está seguindo o livro {book.name}!"
        from_email = os.getenv("EMAIL_HOST_USER")
        to_email = self.request.user.email
        send_mail(subject, message, from_email, [to_email])

        return response


class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
