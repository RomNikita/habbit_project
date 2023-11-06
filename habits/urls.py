from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitAPICreateView, HabitListAPIView, HabitUpdateAPIView, \
    HabitDestroyAPIView, PublicHabitListView

app_name = HabitsConfig.name


urlpatterns = [
    path('habit/create/', HabitAPICreateView.as_view(), name='habit_create'),
    path('habit/list/', HabitListAPIView.as_view(), name='habit_list'),
    path('habit/update/<int:pk>', HabitUpdateAPIView.as_view(), name='habit_update'),
    path('habit/delete/<int:pk>', HabitDestroyAPIView.as_view(), name='habit_delete'),
    path('habit/public/', PublicHabitListView.as_view(), name='public_habit'),
]
