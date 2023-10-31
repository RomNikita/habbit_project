from rest_framework import serializers

from habits.models import Habit
from habits.validators import HabbitRelatedAndAwardValidator, TimeToCompleteValidator, RelatedAndNiceValidator, \
    PeriodicityValidator


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            HabbitRelatedAndAwardValidator(),
            TimeToCompleteValidator(),
            RelatedAndNiceValidator(),
            PeriodicityValidator()
        ]


