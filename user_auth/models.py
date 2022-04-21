from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
