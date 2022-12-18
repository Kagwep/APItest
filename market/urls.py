from django.urls import path, include
from rest_framework import routers
from .views import MarketViewSet

router = routers.DefaultRouter()
router.register(r'', MarketViewSet)

urlpatterns = [
    path('', include(router.urls)),
]