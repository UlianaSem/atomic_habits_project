from datetime import datetime

from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer, IntegerField, PrimaryKeyRelatedField, DateField

from habits.models import Habit, Location
from habits.validators import DurationValidator, PeriodicityValidator, BoundHabitValidator, DayValidator


class HabitSerializer(ModelSerializer):
    bound_habit = PrimaryKeyRelatedField(validators=[BoundHabitValidator()], required=False,
                                         queryset=Habit.objects.all())
    periodicity = IntegerField(validators=[PeriodicityValidator()], required=False)
    duration = IntegerField(validators=[DurationValidator()])
    day = DateField(validators=[DayValidator()], required=False)

    class Meta:
        fields = "__all__"
        model = Habit

    def validate(self, attrs):
        if attrs.get("bound_habit", False) and attrs.get("reward", False):
            raise ValidationError('It is not possible to fill in the "bound_habit" and "reward" '
                                  'fields at the same time')

        if ((attrs.get("is_pleasant", False) is True and attrs.get("bound_habit", False)) or
                (attrs.get("is_pleasant", False) is True and attrs.get("reward", False))):
            raise ValidationError('A pleasant habit cannot have a reward or a bound habit')

        if (attrs.get("day", datetime.utcnow().date()) == datetime.utcnow().date() and
                attrs.get("time") < datetime.utcnow().time()):
            raise ValidationError("There can't be a past tense for today")

        return attrs


class LocationSerializer(ModelSerializer):

    class Meta:
        fields = "__all__"
        model = Location
