from django.db import models


# Create your models here.
class Message(models.Model):
    time = models.DateTimeField(auto_now=True)
    otherParty = models.ForeignKey('invitee.Invitee', related_name='messages', on_delete=models.CASCADE)
    fromMe = models.BooleanField(default=False)
    content = models.TextField()
    isMedia = models.BooleanField(default=False)
    mediaName = models.TextField(default=None, blank=True, null=True)
