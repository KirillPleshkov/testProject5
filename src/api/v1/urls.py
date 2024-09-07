from django.urls import path, include
from rest_framework.routers import DefaultRouter

from src.api.v1.car.views import CarViewSet

router = DefaultRouter()

router.register(r"cars", CarViewSet, basename="api-car")


urlpatterns = [
    path("", include(router.urls)),
]
