from django.db import models

from products.models import Product


class Advertisement(models.Model):
    """Рекламная кампания."""

    name = models.CharField("Название", max_length=200)
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="advertisements",
        verbose_name="Услуга",
    )
    channel = models.CharField("Канал продвижения", max_length=200)
    budget = models.DecimalField("Бюджет", max_digits=10, decimal_places=2)

    class Meta:
        """Метаданные модели рекламной кампании."""

        ordering = ["name"]
        verbose_name = "Рекламная кампания"
        verbose_name_plural = "Рекламные кампании"

    def __str__(self) -> str:  # pylint: disable=invalid-str-returned
        return self.name
