# Generated by Django 5.0.3 on 2024-03-21 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokomizsuariapp', '0023_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Price',
            field=models.IntegerField(),
        ),
    ]
