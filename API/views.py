from django.shortcuts import render
from .serializers import productserializer
from .models import product
from rest_framework import viewsets


# Create your views here.
class productview(viewsets.ModelViewSet):
    queryset = product.objects.all()
    serializer_class = productserializer
