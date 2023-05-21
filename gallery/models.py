from django.db import models
from django.db.models.fields.files import ImageFieldFile


# Create your models here.
class Img(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/country')