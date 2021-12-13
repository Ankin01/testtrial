from django.shortcuts import render

from rest_framework import viewsets

from .serializers import FirmSerializer

from .models import Firm, Product

# Create your views here.

class FirmViewSet(viewsets.ModelViewSet):
    queryset = Firm.objects.all().order_by('name')
    serializer_class = FirmSerializer
