from django.http import Http404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from rest_framework import mixins
from rest_framework import generics

from message.models import Message
from message.serializers import MessageSerializer


class MessageList(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageThread(APIView):
    def get(self, request, otherPartyID):
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)
