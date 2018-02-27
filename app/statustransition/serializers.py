from rest_framework import serializers
from statustransition.models import StatusTransition


class StatusTransitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusTransition
        depth = 1
        fields = ('id', 'time', 'person', 'fromStatus', 'toStatus')
        ordering = ['time']
