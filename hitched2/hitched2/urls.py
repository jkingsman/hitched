from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.authtoken import views

from hitched2.resources import UserViewSet

# from hitched2.views.logout import Logout


# Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'user', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # url(r'^', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^', include('invitee.urls')),
    url(r'^', include('message.urls')),

    # url(r'^login/', views.obtain_auth_token),
    # url(r'^logout/', Logout.as_view()),
]
