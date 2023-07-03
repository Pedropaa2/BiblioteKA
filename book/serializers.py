from rest_framework import serializers
from .models import Book
from users.serializers import UserSerializer


class BookSerializer(serializers.ModelSerializer):
    bookOwner = UserSerializer(read_only=True)

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
            "bookOwner",
        ]

    def create(self, validated_data: dict):
        book = Book.objects.create(**validated_data)
        return book
