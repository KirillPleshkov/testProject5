from rest_framework import serializers

from src.apps.car.models import Car


class CarSerializer(serializers.ModelSerializer):
    """Serializer автомобиля с полной информацией о нем"""

    class Meta:
        model = Car
        fields = "__all__"
