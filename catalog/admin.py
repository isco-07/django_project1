from django.contrib import admin

from catalog.models import Product, Category, Version


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
        "price",
        "category",
    )
    list_filter = ("category",)
    search_fields = (
        "name",
        "description",
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
    )


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
        "number",
        "is_current",
    )
    list_filter = ("is_current",)
    search_fields = (
        "name",
        "number",
    )
