from rest_framework import serializers
from message.models import Message


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'time', 'otherParty', 'fromMe', 'content', 'isMedia', 'mediaName')
