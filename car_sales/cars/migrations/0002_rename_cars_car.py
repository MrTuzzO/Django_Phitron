# Generated by Django 5.1.1 on 2024-11-11 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0001_initial'),
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='cars',
            new_name='Car',
        ),
    ]
