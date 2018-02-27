from django.db import models


# Create your models here.
class Message(models.Model):
    time = models.DateTimeField(auto_now=True)
    otherParty = models.CharField(max_length=13)
    fromMe = models.BooleanField(default=False)
    content = models.TextField()
    isMedia = models.BooleanField(default=False)
    mediaName = models.TextField(default=None, blank=True, null=True)
