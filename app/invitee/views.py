from rest_framework import generics

from invitee.models import Invitee
from invitee.serializers import InviteeSerializer


class InviteeList(generics.ListCreateAPIView):
    queryset = Invitee.objects.all()
    serializer_class = InviteeSerializer


class InviteeDetail(generics.RetrieveUpdateAPIView):
    queryset = Invitee.objects.all()
    serializer_class = InviteeSerializer
