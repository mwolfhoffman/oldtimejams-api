from django.db import models
from django.contrib.auth.models import User


class Jam(models.Model):
    name = models.CharField(max_length=250, default='NO NAME GIVEN')
    city = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    admins = models.ManyToManyField(User)

class Event(models.Model):
    name = models.CharField(max_length=250)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField(max_length=None)
    jam = models.ForeignKey(Jam, on_delete=models.CASCADE)
