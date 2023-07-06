from rest_framework import serializers
from .models import Book, UserBooks
from users.serializers import UserSerializer


class BookSerializer(serializers.ModelSerializer):
    followers = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = [
            "id",
            "name",
            "description",
            "author",
            "publisher",
            "language",
            "publication_date",
            "followers",
        ]


class UserBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBooks
        exclude = ["follow", "book"]
