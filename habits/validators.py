import datetime

from rest_framework import serializers


class HabbitRelatedAndAwardValidator:

    def __call__(self, data):
        is_related_habbit = data.get('is_related_habbit')
        award = data.get('award')

        if is_related_habbit and award:
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
        is_nice_habbit = data.get('is_nice_habbit')
        is_related_habbit = data.get('is_related_habbit')

        if is_related_habbit and is_nice_habbit == False:
            raise serializers.ValidationError("Связанная привычка должна быть приятной привычкой")


class NiceHabbitValidator:
    def __call__(self, data):
        is_nice_habbit = data.get('is_nice_habbit')
        is_related_habbit = data.get('is_related_habbit')
        award = data.get('award')

        if is_nice_habbit == True:
            if award:
                raise serializers.ValidationError(
                    "У приятной привычки не должно быть связанной привычки или награждения")
            if is_related_habbit:
                raise serializers.ValidationError(
                    "У приятной привычки не должно быть связанной привычки или награждения")


class PeriodicityValidator:
    def __call__(self, data):
        periodicity = data.get('periodicity')
        days = ['1', '2', '3', '4', '5', '6', '7']

        if periodicity not in days:
            raise serializers.ValidationError(
                "Привычки должны выполняться не реже, чем 1 раз в 7 дней")