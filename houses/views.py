from .serializers import HouseSerializer
from .models import House
from rest_framework import viewsets, generics


class HouseViewSet(generics.ListCreateAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
