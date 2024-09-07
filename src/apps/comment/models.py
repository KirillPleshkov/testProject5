from django.contrib.auth import get_user_model
from django.db import models

from src.apps.car.models import Car

User = get_user_model()


class Comment(models.Model):
    """Модель комментария к автомобилю"""

    content = models.TextField(verbose_name="содержимое")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="создано")
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="автомобиль",
    )
    author = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="comments", verbose_name="автор"
    )

    class Meta:
        verbose_name = "комментарий"
        verbose_name_plural = "комментарии"

    def __str__(self):
        MAX_CONTENT_LEN = 15
        shortened_content = (
            self.content
            if len(self.content) <= MAX_CONTENT_LEN
            else self.content[:MAX_CONTENT_LEN] + "..."
        )
        return shortened_content
