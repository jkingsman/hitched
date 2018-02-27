from django.db import models


# Create your models here.
class StatusTransition(models.Model):
    time = models.DateTimeField(auto_now=True)
    person = models.ForeignKey('invitee.Invitee', on_delete=models.CASCADE)
    fromStatus = models.TextField()
    toStatus = models.TextField()
