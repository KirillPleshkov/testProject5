from django.urls import path

from src.pages.auth.views import RegistrationView, LoginView
from src.pages.car.views import CarView, CarsView, CreateCarView, ControlCarView

urlpatterns = [
    path("registration/", RegistrationView.as_view(), name="registration"),
    path("login/", LoginView.as_view(), name="login"),
    path("", CarsView.as_view(), name="cars"),
    path("car/<int:id>/", CarView.as_view(), name="car"),
    path("car/create/", CreateCarView.as_view(), name="create-car"),
    path("car/control/<int:id>/", ControlCarView.as_view(), name="control-car"),
]
