from django.contrib import admin

from src.apps.comment.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Запись в админ-панели для сущности комментарий"""

    search_fields = ("content", "author__username")
    autocomplete_fields = ("car", "author")
