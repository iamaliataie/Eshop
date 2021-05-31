from django.contrib import admin

# Register your models here.
from novinfajr_order.models import Order, OrderDetail


class OrderAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'id', 'get_order_total']


class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'price', 'count', 'get_total', 'order_id','get_owner']


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)