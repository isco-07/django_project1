from django.shortcuts import render
from django.views.generic import DetailView, ListView, View

from catalog.models import Product


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name}({phone}): {message}')
    return render(request, 'catalog/contacts.html')


class ProductDetailView(DetailView):
    model = Product


class ProductListView(ListView):
    model = Product


class ContactView(View):
    def get(self, request):
        if request.method == 'POST':
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            print(f'{name}({phone}): {message}')
        return render(request, 'catalog/contacts.html')
