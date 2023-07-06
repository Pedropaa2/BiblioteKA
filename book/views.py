from rest_framework import generics

from app_copy.permissions import AssociateOnlyPermission
from .models import Book
from .serializers import BookSerializer, UserBooksSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Book, UserBooks


class BookListCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AssociateOnlyPermission]
    queryset = Book.objects.all()

    serializer_class = BookSerializer


class FollowBookView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    queryset = UserBooks.objects.all()
    serializer_class = UserBooksSerializer

    def perform_create(self, serializer):
        pk = self.kwargs["pk"]
        book = Book.objects.get(id=pk)
        serializer.save(follow=self.request.user, book=book)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        book_id = self.kwargs["pk"]
        users_following = UserBooks.objects.filter(book_id=book_id).values_list(
            "follow__username", flat=True
        )
        response.data["followers"] = list(users_following)
        return response


class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
