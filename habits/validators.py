import datetime

from rest_framework import serializers


class HabitRelatedAndAwardValidator:

    def __call__(self, data):
        is_related_habit = data.get('is_related_habit')
        award = data.get('award')

        if is_related_habit and award:
            raise serializers.ValidationError(
                "Связанная привычка и указание вознаграждения не могут быть выбраны одновременно.")


class TimeToCompleteValidator:
    def __call__(self, data):
        time_to_complete = data.get('time_to_complete')
        max_time = datetime.timedelta(seconds=120)
        if time_to_complete:
            time_to_complete_datetime = datetime.datetime.combine(datetime.date.min, time_to_complete)

            if time_to_complete_datetime > datetime.datetime.min + max_time:
                raise serializers.ValidationError("Время выполнения не должно превышать 120 секунд.")


class RelatedAndNiceValidator:
    def __call__(self, data):
        is_nice_habit = data.get('is_nice_habit')
        is_related_habit = data.get('is_related_habit')

        if is_related_habit:
            if not is_nice_habit:
                raise serializers.ValidationError("Связанная привычка должна быть приятной привычкой")


class NiceHabitValidator:
    def __call__(self, data):
        is_nice_habit = data.get('is_nice_habit')
        award = data.get('award')
        is_related_habit = data.get('is_related_habit')

        if is_nice_habit:
            if award:
                raise serializers.ValidationError(
                    "У приятной привычки не может быть указано вознаграждение.")
            if is_related_habit:
                raise serializers.ValidationError(
                    "У приятной привычки не может быть связанной привычки.")


class PeriodicityValidator:
    def __call__(self, data):
        periodicity = data.get('periodicity')
        days = ['1', '2', '3', '4', '5', '6', '7']

        if periodicity not in days:
            raise serializers.ValidationError(
                "Привычки должны выполняться не реже, чем 1 раз в 7 дней")