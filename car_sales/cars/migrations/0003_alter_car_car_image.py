# Generated by Django 5.1.1 on 2024-11-11 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_rename_cars_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_image',
            field=models.ImageField(blank=True, null=True, upload_to='cars/media/car_images/'),
        ),
    ]
