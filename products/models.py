from django.db import models


class Product(models.Model):
    """Услуга, предоставляемая компанией."""

    name = models.CharField("Название", max_length=200)
    description = models.TextField("Описание", blank=True)
    cost = models.DecimalField("Стоимость", max_digits=10, decimal_places=2)

    class Meta:
        """Метаданные модели услуги."""

        ordering = ["name"]
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self) -> str:  # pylint: disable=invalid-str-returned
        return self.name
