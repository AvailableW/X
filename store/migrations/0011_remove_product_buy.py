# Generated by Django 4.0.4 on 2022-05-06 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_product_buy_alter_cart_house'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='buy',
        ),
    ]
