from django.db import models


class Brand(models.Model):
    brand_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50,unique= True, null=True, blank=True)

    def __str__(self):
        return self.brand_name
