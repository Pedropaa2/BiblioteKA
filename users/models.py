from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    associate = models.BooleanField(default=False)
    blocked = models.BooleanField(default=False)

    book = models.ManyToManyField(
        "book.Book", through="users.UserBooks", related_name="user_book"
    )


class UserBooks(models.Model):
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="user_marks"
    )

    book = models.ForeignKey(
        "book.Book", on_delete=models.CASCADE, related_name="book_marks"
    )
