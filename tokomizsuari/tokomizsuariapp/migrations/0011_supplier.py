# Generated by Django 5.0.3 on 2024-03-20 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokomizsuariapp', '0010_shipper'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SupplierID', models.IntegerField()),
                ('SupplierName', models.CharField(max_length=25)),
                ('ContactName', models.CharField(max_length=25)),
                ('Address', models.CharField(max_length=25)),
                ('City', models.CharField(max_length=10)),
                ('PostalCode', models.IntegerField()),
                ('Country', models.CharField(max_length=20)),
                ('Phone', models.CharField(max_length=25)),
            ],
        ),
    ]