from rest_framework import serializers
from invitee.models import Invitee


class InviteeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitee
        fields = ('id', 'name', 'phone', 'status')
