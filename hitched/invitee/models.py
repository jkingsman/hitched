from django.db import models

# Create your models here.
class Invitee(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=13)
    status = models.CharField(max_length=200)
