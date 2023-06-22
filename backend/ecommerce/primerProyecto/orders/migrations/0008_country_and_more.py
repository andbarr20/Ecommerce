# Generated by Django 4.2.1 on 2023-06-04 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status_id', models.BooleanField(default=True)),
            ],
        ),
        migrations.RenameField(
            model_name='municipality',
            old_name='department_id',
            new_name='departament',
        ),
        migrations.RemoveField(
            model_name='department',
            name='code',
        ),
        migrations.RemoveField(
            model_name='municipality',
            name='code',
        ),
        migrations.AddField(
            model_name='department',
            name='indicative',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='department',
            name='status_id',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='municipality',
            name='indicative',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='municipality',
            name='status_id',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='address_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='department',
            name='department_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='municipality',
            name='municipality_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='productCategory_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productdetail',
            name='salesCheckDetail_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productinventory',
            name='productInventory_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='salescheck',
            name='salesCheck_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='department',
            name='country',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='orders.country'),
        ),
    ]
