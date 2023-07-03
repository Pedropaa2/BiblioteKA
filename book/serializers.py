from rest_framework import serializers
from .models import Book


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
        ]

    def create(self, validated_data: dict):
        book = Book.objects.create(**validated_data)
        return book
