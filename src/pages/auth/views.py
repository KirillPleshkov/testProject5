from typing import Any

from django.views.generic import TemplateView


class RegistrationView(TemplateView):
    """View для регистрации пользователя"""

    template_name = "user/registration.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(id=id, **kwargs)
        context["title"] = "Регистрация"
        return context


class LoginView(TemplateView):
    """View для авторизации пользователя"""

    template_name = "user/login.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(id=id, **kwargs)
        context["title"] = "Авторизация"
        return context
