from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.name} ({self.description})'

    class Meta:
        verbose_name = 'наименование'
        verbose_name_plural = 'наименования'


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='цена за покупку')
    created_at = models.DateField(**NULLABLE, verbose_name='дата создания')
    updated_at = models.DateField(**NULLABLE, verbose_name='дата изменения')
    manufactured_at = models.DateField(**NULLABLE, verbose_name='дата производства продукта')

    def __str__(self):
        return f'{self.name} ({self.description})'

    class Meta:
        verbose_name = 'наименование'
        verbose_name_plural = 'наименования'
