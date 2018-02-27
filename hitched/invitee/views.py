from django.shortcuts import render

# Create your views here.

from invitee.models import Invitee
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

from invitee.serializers import InviteeSerializer


class InviteeList(generics.ListCreateAPIView):
    queryset = Invitee.objects.all()
    serializer_class = InviteeSerializer


class InviteeDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InviteeSerializer

    def get_queryset(self):
        return Invitee.objects.all()
