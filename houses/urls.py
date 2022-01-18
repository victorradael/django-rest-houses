from django.urls import include, path
from rest_framework import routers
from .views import HouseViewSet

router = routers.DefaultRouter()

houses_url = [
    path('houses/', HouseViewSet.as_view(), name="houses")
]


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    *houses_url
]
