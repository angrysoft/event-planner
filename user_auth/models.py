from django.db import models
from workers.models import User


class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [["user", "token"]]
