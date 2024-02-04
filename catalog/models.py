from django.db import models


class CatalogModel(models.Model):
    """Модель продукты"""
    class Status(models.IntegerChoices):
        DRAFT = 0 # Черновик
        PUBLISHED = 1 # Опубликовано
    name = models.CharField('Наименование',
                            max_length=100,
                            blank=True,
                            unique=True)
    description = models.TextField('Описание',)
    price = models.FloatField('Цена',
                              max_length=10)
    quantity = models.PositiveIntegerField('Количество', 
                                           default=1)
    tags = models.ManyToManyField('TagPost', 
                                  blank=True, 
                                  related_name='tags')
    image = models.ImageField('Фотография', 
                              upload_to='static/media/', 
                              blank=True, 
                              null=True)
    is_published = models.BooleanField('Публикация',
                                       choices=Status.choices,
                                       default=Status.DRAFT)
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('id',)

    def __str__(self) -> str:
        return self.name


class TagPost(models.Model):
    """Модель для тэгов продукта"""
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)

    def __str__(self) -> str:
        return self.tag