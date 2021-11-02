from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StorageSerializer
from .models import persistent_storage
# Create your views here.
class StorageViewSet(viewsets.ModelViewSet):
    queryset = persistent_storage.objects.all().order_by('name')
    serializer_class = StorageSerializer
