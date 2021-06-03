from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from novinfajr_products.models import Product


class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE ,verbose_name='سفارش دهنده')
    payment_date = models.DateTimeField(auto_now=True, blank=True, verbose_name='تاریخ پرداخت')
    is_paid = models.BooleanField(default=False, verbose_name='پرداخت شده/پرداخت نشده')

    def __str__(self):
        return self.owner.username

    def get_order_total(self):
        amount = 0
        for detail in self.orderdetail_set.all():
            amount += detail.price * detail.count
        return amount


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField()
    count = models.IntegerField()

    def __str__(self):
        return self.product.title

    def get_total(self):
        return self.price * self.count

    def get_owner(self):
        return self.order.owner.username