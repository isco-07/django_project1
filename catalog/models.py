from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.name} ({self.description})'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='цена за покупку')
    created_at = models.DateField(**NULLABLE, verbose_name='дата создания')
    updated_at = models.DateField(**NULLABLE, verbose_name='дата изменения')

    def __str__(self):
        return f'{self.name} ({self.description})'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    content = models.TextField(verbose_name='содержимое')
    preview = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='изображение')
    created_at = models.DateField(**NULLABLE, verbose_name='дата создания')
    is_published = models.BooleanField(default=False, verbose_name='опубликовано')
    views_count = models.IntegerField(default=0, verbose_name='просмотры')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Version(models.Model):
    product = models.ForeignKey(Product, related_name='versions', on_delete=models.SET_NULL, default=None, **NULLABLE,
                                verbose_name='продукт')
    number = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='номер')
    name = models.CharField(max_length=50, verbose_name='название')
    is_current = models.BooleanField(verbose_name='текущая')

    def __str__(self):
        return f'{self.number} - {self.name}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
