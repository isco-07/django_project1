# Generated by Django 5.0.3 on 2024-03-17 03:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_category_alter_product_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'категория', 'verbose_name_plural': 'категории'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'продукт', 'verbose_name_plural': 'продукты'},
        ),
    ]