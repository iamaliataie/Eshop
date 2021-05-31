from django.db import models

# Create your models here.


class ClientComment(models.Model):
    name = models.CharField(max_length=200, verbose_name='نام مشتری')
    profession = models.CharField(max_length=255, blank=True, null=True, verbose_name='تخصصص')
    comment = models.TextField(verbose_name='نظر')
    image = models.ImageField(upload_to='clients/', verbose_name='تصویر', null=True, blank=True)

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'

    def __str__(self):
        return self.name