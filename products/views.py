from django.shortcuts import render

# Create your views here.

from rest_framework import serializers, viewsets
from .models import Products




class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('id','name', 'description','added','sold','image')


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = productSerializer