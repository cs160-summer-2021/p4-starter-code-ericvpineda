from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class User(models.Model):
    uid = models.CharField(max_length=100)
    strokeColor = models.CharField(max_length=8)
