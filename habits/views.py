from rest_framework import generics
from habits.models import Habit
from habits.painators import UserHabbitsPaginator
from habits.permissions import IsOwner, CannotEditOrDeletePublicHabit
from habits.serializers import HabitSerializer
from habits.tasks import send_periodic_message


class HabitAPICreateView(generics.CreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    permission_classes = [IsOwner]

    def perform_create(self, serializer):
        new_habit = serializer.save()

        new_habit.user = self.request.user

        new_habit.save()

        send_periodic_message(pk=new_habit.pk)


class HabitListAPIView(generics.ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = UserHabbitsPaginator

    permission_classes = [IsOwner]

    def get_queryset(self):
        user = self.request.user
        return Habit.objects.filter(user=user)


class HabitUpdateAPIView(generics.UpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    permission_classes = [IsOwner]


class HabitDestroyAPIView(generics.DestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    permission_classes = [IsOwner]


class PublicHabitListView(generics.ListAPIView):
    queryset = Habit.objects.filter(is_public=True)
    serializer_class = HabitSerializer
    permission_classes = [CannotEditOrDeletePublicHabit]
