from invitee.models import Invitee
from rest_framework import routers, serializers, viewsets
from invitee.serializers import InviteeSerializer


class InviteeViewSet(viewsets.ModelViewSet):
    queryset = Invitee.objects.all()
    serializer_class = InviteeSerializer
