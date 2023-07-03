from rest_framework import serializers
from .models import Book, UserBooks


class BookSerializer(serializers.ModelSerializer):
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
            "follow",
        ]

    def create(self, validated_data: dict):
        book = Book.objects.create(**validated_data)
        return book


class UserBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBooks
        exclude = ["follow", "book"]
