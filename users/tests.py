from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from users.models import User


class UserRegistrationViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('users:user_register')

    def test_registration_with_valid_data(self):
        data = {
            "email": "testuser@example.com",
            "password": "testpassword",
            "telegram_user_id": 12345
        }
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(email=data['email']).exists())

    def test_registration_with_invalid_data(self):
        data = {
            "email": "invalid_email",
            "password": "testpassword",
            "telegram_user_id": 12345
        }
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(User.objects.filter(email=data['email']).exists())

    def test_registration_with_existing_email(self):
        existing_user = User.objects.create(email="existing@example.com", password="existingpassword")
        data = {
            "email": "existing@example.com",
            "password": "testpassword",
            "telegram_user_id": 12345
        }
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
