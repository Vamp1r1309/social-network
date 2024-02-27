from django.shortcuts import render
from django.views.generic import ListView, FormView

from users.forms import AddRegisterUserForm
from users.models import User
from catalog.models import CatalogModel, TagPost

class CatalogView(ListView):
    model = CatalogModel
    template_name = 'catalog/index.html'
    context_object_name = 'posts'


class UserAuth(FormView):
    """Класс для регистрации
    и авторизации пользователя"""
    model = User
    template_name = 'users/users.html'
    form_class = AddRegisterUserForm
    context_object_name = 'form'