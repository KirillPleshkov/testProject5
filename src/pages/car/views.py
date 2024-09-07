from typing import Any

from django.views.generic import TemplateView

from src.apps.car.models import Car


class CarView(TemplateView):
    """View для отображения списка автомобилей"""

    template_name = "car/cars.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(id=id, **kwargs)
        context["title"] = "Главная"
        context["cars"] = Car.objects.all()
        return context
