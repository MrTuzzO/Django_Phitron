# Generated by Django 5.1.1 on 2024-11-02 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_rename_creaed_on_comment_created_on_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]