from django.conf.urls import url
from invitee import views


urlpatterns = [
    url(r'invitee/$', views.InviteeList.as_view(), name='invitee-list'),
    url(r'invitee/(?P<pk>[0-9]+)/$', views.InviteeDetail.as_view(), name='invitee-detail'),
]
