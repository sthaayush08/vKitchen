# Generated by Django 4.1.6 on 2023-04-23 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='content',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]