from django.db import models

from django_forms import forms
from django.db import models


# Create your models here.
class modelForm(models.Model):
    char_field = models.CharField(max_length=255)
    boolean_field = models.BooleanField()
    binary_field = models.BinaryField()
    date_time_field = models.DateTimeField()
    duration_field = models.DurationField()
    email_field = models.EmailField()
    file_field = models.FileField()
    text_field = models.TextField()
    time_field = models.TimeField()
    url_field = models.URLField()