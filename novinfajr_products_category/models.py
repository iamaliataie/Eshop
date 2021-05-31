from django.db import models

# Create your models here.


class ProductCategory(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان دسته بندی')
    URL = models.SlugField(max_length=200, verbose_name='عنوان در آدرس سایت')
    image = models.ImageField(upload_to='products/category', null=True, verbose_name='تصویر')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/products/category/{self.URL}'