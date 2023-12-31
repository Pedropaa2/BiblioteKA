from django.db import models
from django.utils import timezone


class Book(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    publication_date = models.DateTimeField(default=timezone.now)

    followers = models.ManyToManyField(
        "users.User", through="book.UserBooks", related_name="user_book"
    )


class UserBooks(models.Model):
    follow = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="user_marks"
    )

    book = models.ForeignKey(
        "book.Book", on_delete=models.CASCADE, related_name="book_marks"
    )
