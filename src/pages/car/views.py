from typing import Any

from django.views.generic import TemplateView


class CarView(TemplateView):
    """View для отображения списка автомобилей"""

    template_name = "car/car.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(id=id, **kwargs)
        context["title"] = "Главная"
        return context
