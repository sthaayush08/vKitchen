# Generated by Django 4.1.6 on 2023-04-22 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_product_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
    ]
