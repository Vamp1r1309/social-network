from django.shortcuts import render
from django.views.generic import ListView
from users.models import Users


class CatalogView(ListView):
    ...


class UserAuth(ListView):
    """Класс для регистрации
    и авторизации пользователя"""
    model = Users
    template_name = 'users/users.html'
    context_object_name = 'posts'