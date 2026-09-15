from django.db import models

from products.models import Product


class Contract(models.Model):
    """Контракт на оказание услуги."""

    name = models.CharField("Название", max_length=200)
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="contracts",
        verbose_name="Услуга",
    )
    document = models.FileField("Документ", upload_to="contracts/")
    start_date = models.DateField("Дата заключения")
    end_date = models.DateField("Действует до")
    cost = models.DecimalField("Сумма", max_digits=10, decimal_places=2)

    class Meta:
        """Метаданные модели контракта."""

        ordering = ["-start_date"]
        verbose_name = "Контракт"
        verbose_name_plural = "Контракты"

    def __str__(self) -> str:  # pylint: disable=invalid-str-returned
        return self.name
