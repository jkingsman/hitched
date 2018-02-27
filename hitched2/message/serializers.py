from rest_framework import serializers
from message.models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        depth = 1
        fields = ('id', 'time', 'otherParty', 'fromMe', 'content', 'isMedia', 'mediaName')
        ordering = ['time']
