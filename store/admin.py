from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'article', 'image',
              'description', 'category', 'price',
              'slug', 'stock', 'available',
              'get_image', 'date_add'
              ]
    list_display = ['name', 'price', 'article', 'date_add', 'available', 'get_image']
    list_filter = ['date_add']
    search_fields = ['name', 'article', 'price']
    empty_value_display = '-empty-'
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['get_image', 'date_add']

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="75">')


class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'slug', 'image']
    list_filter = ['name', ]
    search_fields = ['name', ]
    empty_value_display = '-empty-'
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
