from datetime import timedelta

from rest_framework.exceptions import ValidationError

from habits.models import Habit


class DurationValidator:

    def __call__(self, value):
        if value > 120:
            raise ValidationError("Duration should be less 120 sec")


class PeriodicityValidator:

    def __call__(self, value):
        if value > timedelta(days=7):
            raise ValidationError("Periodicity should be less 7 days")


class BoundHabitValidator:

    def __call__(self, value):
        habit = Habit.objects.get(pk=value)

        if not habit.is_pleasant:
            raise ValidationError("Habit should have the hallmark of a pleasant habit")
