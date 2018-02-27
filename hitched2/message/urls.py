from django.conf.urls import url
from message import views


urlpatterns = [
    url(r'^message/$', views.rawMessageDump),
    url(r'^message/(?P<otherParty>[0-9]+)/$', views.messageThread),
]
