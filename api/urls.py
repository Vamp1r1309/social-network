from django.contrib import admin
from django.urls import path

from api.views import UserAuth, CatalogView

name = 'api'

urlpatterns = [
    path('', CatalogView.as_view(), name="home"),
    path('auth/', UserAuth.as_view(), name='authorization')
]
