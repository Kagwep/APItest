from django.shortcuts import render

# Create your views here.

from rest_framework import serializers, viewsets
from .models import Market




class marketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = ('id','name', 'description','created','image','location')


class MarketViewSet(viewsets.ModelViewSet):
    queryset = Market.objects.all()
    serializer_class = marketsSerializer