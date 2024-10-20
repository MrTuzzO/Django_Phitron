# Generated by Django 5.1.1 on 2024-10-20 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='modelForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('char_field', models.CharField(max_length=255)),
                ('boolean_field', models.BooleanField()),
                ('binary_field', models.BinaryField()),
                ('date_time_field', models.DateTimeField()),
                ('duration_field', models.DurationField()),
                ('email_field', models.EmailField(max_length=254)),
                ('file_field', models.FileField(upload_to='')),
                ('text_field', models.TextField()),
                ('time_field', models.TimeField()),
                ('url_field', models.URLField()),
            ],
        ),
    ]
