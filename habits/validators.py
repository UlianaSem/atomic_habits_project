from datetime import date

from rest_framework.exceptions import ValidationError


class DurationValidator:

    def __call__(self, value):
        if value > 120:
            raise ValidationError("Duration should be less 120 sec")


class PeriodicityValidator:

    def __call__(self, value):
        if value > 7:
            raise ValidationError("Periodicity should be not more 7 days")


class BoundHabitValidator:

    def __call__(self, value):

        if not value.is_pleasant:
            raise ValidationError("Habit should have the hallmark of a pleasant habit")


class DayValidator:

    def __call__(self, value):
        if value < date.today():
            raise ValidationError("A day can't be past")
