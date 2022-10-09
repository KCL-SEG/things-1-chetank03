from unicodedata import name
from django.db import models
from django.db.models import Model


class Thing(Model):
    name = models.TextField()
    description = models.TextField()
    quantity = models.IntegerField()
