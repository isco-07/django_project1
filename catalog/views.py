from django.shortcuts import render

from catalog.models import Product, Category


def home(request):
    context = {
        'objects_list': Category.objects.all(),
        'title': 'Магазин'
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name}({phone}): {message}')
    return render(request, 'catalog/contacts.html')


def category(request, pk):
    context = {
        'category': Product.objects.filter(category=pk),
        'title': 'Список товаров'
    }
    return render(request, 'catalog/category.html', context)


def product(request, pk):
    context = {
        'product': Product.objects.get(pk=pk)
    }
    return render(request, 'catalog/product.html', context)
