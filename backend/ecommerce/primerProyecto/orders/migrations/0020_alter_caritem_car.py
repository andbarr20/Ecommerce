# Generated by Django 4.2.1 on 2023-06-12 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0019_delete_salescheck'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caritem',
            name='car',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.car'),
        ),
    ]