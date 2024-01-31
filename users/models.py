from django.db import models

# Create your models here.

class Users(models.Model):
    """Модель создания пользователя"""
    username = models.CharField("Имя пользователя",
                                max_length=50,
                                unique=True,
                                blank=True)
    password = models.CharField('Пароль',
                                max_length=50,
                                blank=True)