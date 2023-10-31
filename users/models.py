from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None

    email = models.EmailField(max_length=150, verbose_name='электронная почта', unique=True)
    password = models.CharField(max_length=100, verbose_name='пароль')
    phone = models.CharField(max_length=50, unique=True, verbose_name='номер телефона', null=True, blank=True)
    avatar = models.ImageField(upload_to='user', null=True, blank=True, verbose_name='аватар')
    country = models.CharField(max_length=40, null=True, blank=True, verbose_name='страна')
    is_active = models.BooleanField(default=True, verbose_name='признак верификации')
    telegram_user_id = models.IntegerField(default=0, verbose_name='чат ID пользователя')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []