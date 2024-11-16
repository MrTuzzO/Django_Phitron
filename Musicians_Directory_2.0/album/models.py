from django.db import models
from musician.models import Musician

# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=255)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE, related_name='albums')
    release_date = models.DateField(auto_now_add=True)
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
        return self.album_name