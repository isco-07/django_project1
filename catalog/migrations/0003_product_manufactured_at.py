# Generated by Django 5.0.3 on 2024-03-17 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_category_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='manufactured_at',
            field=models.DateField(blank=True, null=True, verbose_name='дата производства продукта'),
        ),
    ]
