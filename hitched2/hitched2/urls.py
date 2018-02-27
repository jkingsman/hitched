from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.authtoken import views

from hitched2.views.logout import Logout

urlpatterns = [
    url(r'^api', include('invitee.urls')),
    url(r'^api', include('message.urls')),

    url(r'^api/get-token/', views.obtain_auth_token),
    url(r'^api/discard-token/', Logout.as_view()),
]
