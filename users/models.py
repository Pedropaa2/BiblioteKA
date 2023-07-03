from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    associate = models.BooleanField(default=False)
    blocked = models.BooleanField(default=False)
