from django.http import Http404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from rest_framework import mixins
from rest_framework import generics

from invitee.models import Invitee
from message.models import StatusTransition
from message.serializers import StatusTransitionSerializer


class PersonTransition(APIView):
    def get(self, request, personID):
        messages = StatusTransition.objects.filter(person=Invitee(id=personID))
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)
