from django.db import models


class CatalogModel(models.Model):
    name = models.CharField('Наименование',
                            max_length=100,
                            blank=True,
                            unique=True)
    description = models.TextField('Описание',)
    price = models.FloatField('Цена',
                              max_length=10)
    quantity = models.IntegerField('Количество')
    tags = models.ManyToManyField('TagPost', blank=True, related_name='tags')

class TagPost(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)

    def __str__(self) -> str:
        return self.tag