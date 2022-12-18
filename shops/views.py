from django.shortcuts import render

# Create your views here.

from rest_framework import serializers, viewsets
from .models import Shops




class shopsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shops
        fields = ('id','name', 'description','created','image','website','phone','location','area_code','code')


class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shops.objects.all()
    serializer_class = shopsSerializer