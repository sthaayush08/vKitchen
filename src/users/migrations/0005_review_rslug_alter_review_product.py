# Generated by Django 4.1.6 on 2023-04-22 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_product_slug'),
        ('users', '0004_alter_review_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rslug',
            field=models.SlugField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='review',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
    ]
