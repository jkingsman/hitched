from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view

from message.models import Message
from message.serializers import MessageSerializer

@api_view(['GET'])
def rawMessageDump(request):
    if request.method == 'GET':
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['GET'])
def messageThread(request, otherParty):
    try:
        messages = Message.objects.filter(otherParty=otherParty)
        serializer = MessageSerializer(messages, many=True)
        return JsonResponse(serializer.data, safe=False)
    except Message.DoesNotExist:
        return HttpResponse(status=404)
