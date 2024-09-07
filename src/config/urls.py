from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/", include("api.auth.urls")),
    path("api/", include("api.v1.urls")),
    path("", include("pages.urls")),
]
