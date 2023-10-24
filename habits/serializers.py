from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer, IntegerField, DurationField

from habits.models import Habit
from habits.validators import DurationValidator, PeriodicityValidator, BoundHabitValidator


class HabitSerializer(ModelSerializer):
    bound_habit = IntegerField(validators=[BoundHabitValidator()], required=False)
    periodicity = DurationField(validators=[PeriodicityValidator()], required=False)
    duration = IntegerField(validators=[DurationValidator()])

    class Meta:
        fields = "__all__"
        model = Habit

    def create(self, validated_data):
        bound_habit = validated_data.get("bound_habit")
        if bound_habit:
            return Habit.objects.get(pk=bound_habit)

    def validate(self, attrs):
        if attrs.get("bound_habit", False) and attrs.get("reward", False):
            raise ValidationError('It is not possible to fill in the "bound_habit" and "reward" '
                                  'fields at the same time')

        if ((attrs.get("is_pleasant", False) is True and attrs.get("bound_habit", False)) or
                (attrs.get("is_pleasant", False) is True and attrs.get("reward", False))):
            raise ValidationError('A pleasant habit cannot have a reward or a bound habit')

        return attrs
