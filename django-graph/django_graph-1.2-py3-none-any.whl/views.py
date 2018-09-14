from django.http import HttpResponse
from rest_framework import viewsets

from .models import *
from .serializers import *


class EndpointViewSet(viewsets.ModelViewSet):
    queryset = Endpoint.objects.all()
    serializer_class = EndpointSerializer


class CounterViewSet(viewsets.ModelViewSet):
    queryset = Counter.objects.all()
    serializer_class = CounterSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
