from rest_framework import serializers
from invitee.models import Invitee


class InviteeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Invitee
        fields = ('id', 'name', 'phone', 'status')
        extra_kwargs = {
            'url': {
                'view_name': 'invitee:invitee-detail',
            }
        }
