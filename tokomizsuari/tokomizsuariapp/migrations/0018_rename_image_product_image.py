# Generated by Django 5.0.3 on 2024-03-21 01:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tokomizsuariapp', '0017_remove_customer_image_display_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Image',
            new_name='image',
        ),
    ]
