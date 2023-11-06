from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Habit(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='пользователь', **NULLABLE)
    place = models.CharField(max_length=150, verbose_name='место')
    time = models.TimeField(verbose_name='время привычки')
    action = models.CharField(max_length=200, verbose_name='действие')
    is_nice_habit = models.BooleanField(default=False, verbose_name='приятная привычка', **NULLABLE)
    is_related_habit = models.ForeignKey('self', verbose_name='связанная привычка', on_delete=models.CASCADE, **NULLABLE)
    periodicity = models.CharField(max_length=10, default='1', verbose_name='переодичность')
    award = models.CharField(max_length=100, verbose_name='вознаграждение', **NULLABLE)
    time_to_complete = models.TimeField(verbose_name='время на выполнение')
    is_public = models.BooleanField(default=True, verbose_name='признак публичности')

    def __str__(self):
        return f'Я буду {self.action} в {self.time} в {self.place}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'

