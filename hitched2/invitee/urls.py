from django.conf.urls import url
from invitee import views


urlpatterns = [
    url(r'^invitee/$', views.inviteeList),
    url(r'^invitee/(?P<pk>[0-9]+)/$', views.inviteeDetail),
]
