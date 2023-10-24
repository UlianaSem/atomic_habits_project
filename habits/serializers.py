from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer, IntegerField, DurationField, PrimaryKeyRelatedField

from habits.models import Habit, Location
from habits.validators import DurationValidator, PeriodicityValidator, BoundHabitValidator


class HabitSerializer(ModelSerializer):
    bound_habit = PrimaryKeyRelatedField(validators=[BoundHabitValidator()], required=False,
                                         queryset=Habit.objects.all())
    periodicity = DurationField(validators=[PeriodicityValidator()], required=False)
    duration = IntegerField(validators=[DurationValidator()])

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

        return attrs


class LocationSerializer(ModelSerializer):

    class Meta:
        fields = "__all__"
        model = Location
