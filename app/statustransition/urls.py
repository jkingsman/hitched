from django.conf.urls import url
from statustransition import views


urlpatterns = [
    url(r'statustransition/(?P<personID>[0-9]+)/$', views.PersonTransition.as_view(), name='person-transitions'),
]
