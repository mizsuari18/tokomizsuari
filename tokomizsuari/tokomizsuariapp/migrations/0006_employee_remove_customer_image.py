# Generated by Django 5.0.3 on 2024-03-20 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokomizsuariapp', '0005_rename_image_customer_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EmployeeID', models.IntegerField()),
                ('LastName', models.CharField(max_length=25)),
                ('FirstName', models.CharField(max_length=25)),
                ('BirthDate', models.DateField()),
                ('Photo', models.ImageField(blank=True, null=True, upload_to='images')),
                ('Notes', models.TextField(blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='customer',
            name='Image',
        ),
    ]