from django.db import models
import os


# Create your models here.
from django.http import Http404

from novinfajr_products_category.models import ProductCategory


def get_file_ext(file):
    base_name = os.path.basename(file)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_path(instance, filename):
    name, ext = get_file_ext(filename)
    final_name = f'{instance.title}{ext}'
    return f'products/{final_name}'


class ProductManager(models.Manager):
    def get_porduct_by_id(self, prodcutId):
        query = self.get_queryset().filter(id=prodcutId)
        if query.count() == 1:
            return query.first()
        else:
            raise Http404('ایتم یافت نشد')

    def get_product_by_category(self, category_ame):
        return self.get_queryset().filter(category__URL__iexact=category_ame)


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='نام کالا')
    description = models.TextField(verbose_name='توضیحات')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='قیمت')
    image = models.ImageField(upload_to=upload_path, verbose_name='تصویر')
    category = models.ForeignKey(ProductCategory, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.title

    objects = ProductManager()

    def get_absolute_url(self):
        return f'/product/{self.id}/{self.title.replace(" ", "-")}'
