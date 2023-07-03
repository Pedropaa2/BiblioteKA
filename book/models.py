from django.db import models
from django.utils import timezone


class Book(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    publication_date = models.DateTimeField(default=timezone.now)
