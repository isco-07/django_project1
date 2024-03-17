import json

from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        try:
            with open('category_data.json') as f:
                json_loader = json.load(f)
            category_list = []
            for item in json_loader:
                if item['model'] == "catalog.category":
                    category_list.append({'name': item['fields']['name'],
                                          'description': item['fields']['description']})
            return category_list
        except Exception:
            raise Exception

    @staticmethod
    def json_read_products():
        try:
            with open('category_data.json') as f:
                json_loader = json.load(f)
            product_list = []
            for item in json_loader:
                if item['model'] == "catalog.product":
                    product_list.append({'name': item['fields']['name'],
                                         'description': item['fields']['description'],
                                         'image': item['fields']['image'],
                                         'category': item['fields']['category'],
                                         'price': item['fields']['price'],
                                         'created_at': item['fields']['created_at'],
                                         'updated_at': item['fields']['updated_at'],
                                         })
            return product_list
        except Exception:
            raise Exception

    def handle(self, *args, **options):

        # Удалите все продукты
        Product.objects.all().delete()
        # Удалите все категории
        Category.objects.all().delete()

        # Создайте списки для хранения объектов
        product_for_create = []
        category_for_create = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            category_for_create.append(
                Category(**category)
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for product in Command.json_read_products():
            product_for_create.append(
                Product(**product)
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)
