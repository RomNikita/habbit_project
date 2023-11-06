import json

from celery import shared_task
from django_celery_beat.models import PeriodicTask, CrontabSchedule

from config import settings
from habits.models import Habit
from habits.services import send_telegram_message


@shared_task
def send_habit_message(habit_id, chat_id, token):
    habit = Habit.objects.get(pk=habit_id)
    message = str(habit)
    send_telegram_message(chat_id, message, token)


def send_periodic_message(pk):
    habit = Habit.objects.get(pk=pk)

    chat_id = habit.user.telegram_user_id
    token = settings.TELEGRAM_BOT_TOKEN

    if chat_id is not None:
        if habit.periodicity == '1':
            schedule, _ = CrontabSchedule.objects.get_or_create(minute=habit.time.minute, hour=habit.time.hour)
        elif habit.periodicity == '2':
            schedule, _ = CrontabSchedule.objects.get_or_create(minute=habit.time.minute, hour=habit.time.hour,
                                                                day_of_month='*/2')
        elif habit.periodicity == '3':
            schedule, _ = CrontabSchedule.objects.get_or_create(minute=habit.time.minute, hour=habit.time.hour,
                                                                day_of_month='*/3')
        elif habit.periodicity == '4':
            schedule, _ = CrontabSchedule.objects.get_or_create(minute=habit.time.minute, hour=habit.time.hour,
                                                                day_of_month='*/4')
        elif habit.periodicity == '5':
            schedule, _ = CrontabSchedule.objects.get_or_create(minute=habit.time.minute, hour=habit.time.hour,
                                                                day_of_month='*/5')
        elif habit.periodicity == '6':
            schedule, _ = CrontabSchedule.objects.get_or_create(minute=habit.time.minute, hour=habit.time.hour,
                                                                day_of_month='*/6')
        elif habit.periodicity == '7':
            schedule, _ = CrontabSchedule.objects.get_or_create(minute=habit.time.minute, hour=habit.time.hour,
                                                                day_of_month='*/7')
        else:
            schedule, _ = CrontabSchedule.objects.get_or_create(minute=habit.time.minute, hour=habit.time.hour)
        print('test')
        periodic_task = PeriodicTask.objects.create(
            crontab=schedule,
            name=f'Sending Telegram Message for {habit.id}',
            task='habits.tasks.send_habit_message',
            args=json.dumps([habit.id, chat_id, token]),
        )

        periodic_task.enabled = True
        periodic_task.save()


