from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Car(models.Model):
    """Модель автомобиля"""

    make = models.CharField(max_length=100, verbose_name="марка")
    model = models.CharField(max_length=100, verbose_name="модель")
    year = models.PositiveIntegerField(verbose_name="год выпуска")
    description = models.TextField(verbose_name="описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="создано")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="обновлено")
    owner = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="car", verbose_name="владелец"
    )

    class Meta:
        verbose_name = "автомобиль"
        verbose_name_plural = "автомобили"
        ordering = ["-id"]

    def __str__(self):
        return f"{self.make} {self.model} {self.year}г"
