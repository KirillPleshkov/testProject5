from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from src.apps.car.models import Car
from src.apps.car.serializers import CarSerializer


class CarViewSet(viewsets.ViewSet):
    """VewSet для сущности "Автомобиль", методы: list, retrieve, create, destroy, update"""

    serializer_class = CarSerializer
    queryset = Car.objects.all()

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
