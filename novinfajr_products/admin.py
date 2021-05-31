from django.contrib import admin

# Register your models here.
from novinfajr_products.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'id', 'price']


admin.site.register(Product, ProductAdmin)