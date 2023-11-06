from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import Habit
from users.models import User

class HabitTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(email='testuser@example.com', password='testpassword')
        self.client.force_authenticate(user=self.user)

    def test_create_habit(self):
        url = reverse('main:habit_create')
        data = {
            'place': 'Test Place',
            'time': '10:00:00',
            'action': 'Test Action',
            'is_nice_habit': False,
            'is_related_habit': None,
            'periodicity': '1',
            'award': None,
            'time_to_complete': '00:02:00',
            'is_public': True
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_habit(self):
        habit = Habit.objects.create(
            user=self.user,
            place='Test Place',
            time='10:00:00',
            action='Test Action',
            is_public=True,
            time_to_complete='00:02:00',
            periodicity='1')
        url = reverse('main:habit_update', args=[habit.id])

        data = {
            'user': self.user.pk,
            'place': 'Update',
            'time': '11:00:00',
            'action': 'Updated Action',
            'time_to_complete': '00:02:00',
            'is_public': 'false',
            'award': 'food',
            'periodicity': '1',

        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)
        updated_habit = Habit.objects.get(id=habit.id)
        self.assertEqual(updated_habit.place, 'Update')

    def test_delete_habit(self):
        habit = Habit.objects.create(
            user=self.user,
            place='Test Place',
            time='10:00:00',
            action='Test Action',
            is_public=True,
            time_to_complete='00:02:00')
        url = reverse('main:habit_delete', args=[habit.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Habit.objects.filter(id=habit.id).exists())

    def test_permission(self):
        habit = Habit.objects.create(
            user=self.user,
            place='Test Place',
            time='10:00:00',
            action='Test Action',
            is_public=True,
            time_to_complete='00:02:00')
        another_user = User.objects.create(email='anotheruser@example.com', password='anotherpassword')
        self.client.force_authenticate(user=another_user)

        url = reverse('main:habit_update', args=[habit.id])
        data = {'place': 'Updated Place'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_validators(self):
        url = reverse('main:habit_create')
        data = {
            'place': 'Test Place',
            'time': '10:00:00',
            'action': 'Test Action',
            'is_nice_habit': True,
            'is_related_habit': None,
            'periodicity': '8',
            'award': 'Test Award',
            'time_to_complete': '00:02:30',
            'is_public': True
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
