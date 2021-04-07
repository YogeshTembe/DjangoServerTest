
from django.db import models
#from djangotoolbox import fields
from rest_framework import serializers
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Movie(models.Model):
    title=models.CharField(max_length=32)
    desc=models.CharField(max_length=5000)
    year=models.IntegerField()


    

