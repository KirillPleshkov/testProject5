from django.contrib import admin

from .models import Car
from ..comment.models import Comment


class CommentInline(admin.TabularInline):
    """Список комментариев для сущности "автомобиль" админ-панели"""

    model = Comment
    extra = 0


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    """Запись в админ-панели для сущности автомобиль"""

    search_fields = ("make", "model", "year", "owner__username")
    autocomplete_fields = ("owner",)
    list_display = ("__str__", "owner")
    inlines = (CommentInline,)
