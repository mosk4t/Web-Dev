from django.contrib import admin
from .models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'count', 'is_active', 'category')
    list_filter = ('is_active', 'category')
    search_fields = ('name', 'description')
    list_editable = ('price', 'count', 'is_active')