from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.authtoken import views

from hitched2.views.logout import Logout

urlpatterns = [
    url(r'^', include('invitee.urls')),
    url(r'^', include('message.urls')),

    url(r'^login/', views.obtain_auth_token),
    url(r'^logout/', Logout.as_view()),
]
