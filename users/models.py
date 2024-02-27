from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель создания пользователя"""
    email = models.EmailField(
        'Email',
        max_length=70,
        unique=True
    )
    first_name = models.CharField(
        "Имя пользователя",
        max_length=50)
    last_name = models.CharField(
        'Фамилия',
        max_length=50)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self) -> str:
        return self.email