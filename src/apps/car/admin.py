from django.contrib import admin

from .models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    """Запись в админ-панели для сущности автомобиль"""

    search_fields = ("make", "model", "year", "owner__username")
    autocomplete_fields = ("owner",)
