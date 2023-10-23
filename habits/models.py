from datetime import timedelta

from django.conf import settings
from django.db import models


NULLABLE = {"blank": True, "null": True}


class Location(models.Model):
    location = models.CharField(max_length=200, verbose_name="место", unique=True)

    def __str__(self):
        return f"{self.location}"

    class Meta:
        verbose_name = "место"
        verbose_name_plural = "места"


class Habit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="пользователь", on_delete=models.CASCADE)

    location = models.ForeignKey(Location, on_delete=models.SET_DEFAULT, verbose_name="место", default="любое место")
    bound_habit = models.ForeignKey("Habit", on_delete=models.SET_NULL, verbose_name="связанная привычка", **NULLABLE)

    periodicity = models.DurationField(verbose_name="Периодичность", default=timedelta(days=1))
    time = models.TimeField(verbose_name="время")
    action = models.CharField(max_length=300, verbose_name="действие")
    duration = models.PositiveIntegerField(verbose_name="Время на выполнение")
    reward = models.CharField(max_length=400, verbose_name="Вознаграждение", **NULLABLE)

    is_pleasant = models.BooleanField(verbose_name="приятная привычка")
    is_public = models.BooleanField(default=False, verbose_name="видна всем")

    def __str__(self):
        return f"я буду {self.action} в {self.time} в {self.location}"

    class Meta:
        verbose_name = "привычка"
        verbose_name_plural = "привычки"
