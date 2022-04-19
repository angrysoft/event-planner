from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class Token(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField()
    refresh_token = models.CharField()
    created = models.DateTimeField(auto_now_add=True)
