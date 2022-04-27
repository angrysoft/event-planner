from django.db import models
from django.utils.translation import gettext_lazy as _
from workers.models import User


class Event(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Event name"))
    number = models.CharField(
        max_length=50, verbose_name=_("Event number"), unique=True
    )

    def __str__(self):
        return f"{self.name}-{self.number}"


class EventSchedule(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE)
    day = models.DateField()
    info = models.TextField()


class EventWorkerDay(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE)
    function = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name=_("Function")
    )
    start = models.DateTimeField()
    end = models.DateTimeField()


class Venue(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()


class EventInfo(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.PROTECT, related_name="venue")
    coordinator = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="event_coordinator",
        verbose_name="Koordynator",
    )
    sales = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="event_sales",
        verbose_name="Handlowiec",
    )
    comments = models.TextField(verbose_name="Uwagi", default="", blank=True)

    def __str__(self):
        return str(self.event)
