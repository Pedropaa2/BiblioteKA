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

        def validate(self, attrs):
            user_email = self.context["request"].user.email
            book = attrs["book"]

            # Verificar se já existe um registro com o mesmo email do usuário
            if UserBooks.objects.filter(follow__email=user_email, book=book).exists():
                raise serializers.ValidationError("Você já está seguindo este livro.")

            return attrs
