from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, View, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from catalog.models import Product, Blog


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


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content')
    success_url = reverse_lazy('catalog:blog_list')

    def form_valid(self, form):
        if form.is_valid:
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()
        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content')
    success_url = reverse_lazy('catalog:blog_list')

    def get_success_url(self):
        return reverse('catalog:blog_view', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog_list')
