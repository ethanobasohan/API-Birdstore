from rest_framework import generics
from .models import Bird
from .serializers import BirdSerializer


class BirdListCreate(generics.ListCreateAPIView):
    queryset = Bird.objects.all()
    serializer_class = BirdSerializer


class BirdDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bird.objects.all()
    serializer_class = BirdSerializer
    lookup_field = 'name'


