# Generated by Django 4.1.6 on 2023-04-23 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_remove_product_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-created_date']},
        ),
    ]
