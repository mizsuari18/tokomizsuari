# Generated by Django 5.0.3 on 2024-03-20 04:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tokomizsuariapp', '0004_customer_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='image',
            new_name='Image',
        ),
    ]
