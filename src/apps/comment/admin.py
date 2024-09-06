from django.contrib import admin

from src.apps.comment.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Запись в админ-панели для сущности комментарий"""

    search_fields = (
        "content",
        "car__make",
        "car__model",
        "car__year",
        "author__username",
    )
    autocomplete_fields = ("car", "author")
    list_display = ("__str__", "car", "author")
