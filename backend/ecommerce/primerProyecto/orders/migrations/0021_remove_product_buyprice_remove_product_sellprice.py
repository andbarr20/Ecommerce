# Generated by Django 4.2.1 on 2023-06-12 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0020_alter_caritem_car'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='buyPrice',
        ),
        migrations.RemoveField(
            model_name='product',
            name='sellPrice',
        ),
    ]