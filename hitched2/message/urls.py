from django.conf.urls import url
from message import views


urlpatterns = [
    url(r'^message/$', views.MessageList.as_view()),
    url(r'^message/(?P<otherPartyID>[0-9]+)/$', views.MessageThread.as_view()),
]
