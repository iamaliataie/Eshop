# Generated by Django 3.2.3 on 2021-06-03 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novinfajr_order', '0003_orderdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='تاریخ پرداخت'),
        ),
    ]
