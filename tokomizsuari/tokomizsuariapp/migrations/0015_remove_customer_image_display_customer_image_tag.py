# Generated by Django 5.0.3 on 2024-03-21 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokomizsuariapp', '0014_rename_image_customer_image_display'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='image_display',
        ),
        migrations.AddField(
            model_name='customer',
            name='image_tag',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
