from ast import mod
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class Skill(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Skill")


class Cooperation(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Form of coopertion")


class User(AbstractUser):
    nickname = models.CharField(max_length=50, verbose_name=_("Nickname"))
    phone = models.CharField(
        max_length=15, verbose_name=_("Phone"), default=0, blank=True
    )
    skills = models.ManyToManyField(Skill, verbose_name=_("Skills"))

    def __str__(self):
        return f"{self.first_name} {self.last_name} <{self.nickname}>"

    class Meta:
        unique_together = [["first_name", "last_name"]]
