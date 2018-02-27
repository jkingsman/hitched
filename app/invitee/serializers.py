from rest_framework import serializers
from invitee.models import Invitee


class InviteeSerializer(serializers.ModelSerializer):
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.status = validated_data.get('status', instance.status)
        instance.created = validated_data.get('created', instance.created)

        instance.save()
        return instance

    class Meta:
        model = Invitee
        fields = ('id', 'name', 'phone', 'status')
