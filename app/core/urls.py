from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.authtoken import views

from core.views.logout import Logout

urlpatterns = [
    url(r'^', include('invitee.urls')),
    url(r'^', include('message.urls')),

    url(r'^get-token/', views.obtain_auth_token),
    url(r'^discard-token/', Logout.as_view()),
]
