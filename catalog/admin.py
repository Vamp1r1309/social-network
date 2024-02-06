from django.contrib import admin

from catalog.models import CatalogModel
# Register your models here.


@admin.register(CatalogModel)
class CatalogAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'description', 'price',
        'quantity', 'image', 'is_published'
    )