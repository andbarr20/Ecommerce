# Generated by Django 4.2.1 on 2023-06-12 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_profile_city_profile_country_profile_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='indicative',
        ),
        migrations.RemoveField(
            model_name='department',
            name='status_id',
        ),
    ]
