from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductDetailView, ProductListView, ContactView, BlogListView, BlogDetailView, \
    BlogCreateView, BlogUpdateView, BlogDeleteView

app_name = CatalogConfig.name
urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_view'),
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('view/<int:pk>', BlogDetailView.as_view(), name='blog_view'),
    path('create/', BlogCreateView.as_view(), name='blog_create'),
    path('edit/<int:pk>', BlogUpdateView.as_view(), name='blog_update'),
    path('delete/<int:pk>', BlogDeleteView.as_view(), name='blog_delete'),
]
