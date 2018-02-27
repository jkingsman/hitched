from django.http import Http404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from rest_framework import mixins
from rest_framework import generics

from message.models import Message
from message.serializers import MessageSerializer


class MessageList(APIView):
    def get(self, request):
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            # phone logic goes here

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MessageThread(APIView):
    def get(self, request, otherPartyID):
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)
