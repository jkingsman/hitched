from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view

from invitee.models import Invitee
from invitee.serializers import InviteeSerializer


@api_view(['GET', 'POST'])
def inviteeList(request):
    if request.method == 'GET':
        invitees = Invitee.objects.all()
        serializer = InviteeSerializer(invitees, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = InviteeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'PATCH'])
def inviteeDetail(request, pk):
    try:
        invitee = Invitee.objects.get(pk=pk)
    except Invitee.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = InviteeSerializer(invitee)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = InviteeSerializer(invitee, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        invitee.delete()
        return HttpResponse(status=204)
