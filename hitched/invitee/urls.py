from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from invitee import views


urlpatterns = [
    url(r'^invitee/$', views.InviteeList.as_view(), name='invitee-list'),
    url(r'^invitee/(?P<pk>[0-9]+)/$', views.InviteeDetail.as_view(), name='invitee-detail'),
]
