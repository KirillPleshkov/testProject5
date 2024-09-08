from django.urls import path

from src.pages.auth.views import RegistrationView, LoginView
from src.pages.car.views import CarView, CarsView

urlpatterns = [
    path("registration/", RegistrationView.as_view(), name="registration"),
    path("login/", LoginView.as_view(), name="login"),
    path("", CarsView.as_view(), name="cars"),
    path("car/<int:id>/", CarView.as_view(), name="car"),
]
