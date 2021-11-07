from django.db import models


# Create your models here.

class Planets(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    custom_name = models.CharField(max_length=200)
    created = models.DateTimeField()
    edited = models.DateTimeField()
    url = models.CharField(max_length=500)
    is_favorite = models.BooleanField(default=False)


class Movies(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    custom_title = models.CharField(max_length=200, default='')
    created = models.DateTimeField()
    edited = models.DateTimeField()
    release_date = models.DateField()
    url = models.CharField(max_length=500)
    is_favorite = models.BooleanField(default=False)
