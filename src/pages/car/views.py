from typing import Any

from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from src.apps.car.models import Car


class CarsView(TemplateView):
    """View для отображения списка автомобилей"""

    template_name = "car/cars.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(id=id, **kwargs)
        context["title"] = "Главная"
        context["cars"] = Car.objects.all()
        return context


class CarView(TemplateView):
    """View для отображения списка автомобилей"""

    template_name = "car/car.html"

    def get_context_data(self, id: int, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(id=id, **kwargs)
        context["title"] = "Главная"
        context["car"] = get_object_or_404(Car, id=id)
        return context
