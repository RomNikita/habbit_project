from rest_framework import serializers

from habits.models import Habit
from habits.validators import HabitRelatedAndAwardValidator, TimeToCompleteValidator, RelatedAndNiceValidator, \
    PeriodicityValidator, NiceHabitValidator


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            HabitRelatedAndAwardValidator(),
            TimeToCompleteValidator(),
            RelatedAndNiceValidator(),
            PeriodicityValidator(),
            NiceHabitValidator()
        ]


