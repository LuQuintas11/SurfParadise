from django.contrib import admin
from .models import Product, Category, Review

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
  
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ( 'body', 'product', 'created_on')
    search_fields = ('name', 'email', 'body')

    

