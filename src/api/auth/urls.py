from dj_rest_auth.jwt_auth import get_refresh_view
from dj_rest_auth.views import LoginView


from rest_framework_simplejwt.views import TokenVerifyView
from django.urls import path

from src.api.auth.views import RegisterUser

urlpatterns = [
    path("register/", RegisterUser.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("token/refresh/", get_refresh_view().as_view(), name="token_refresh"),
]
