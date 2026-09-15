from django.db import models

from advertisements.models import Advertisement


class Lead(models.Model):
    """Потенциальный клиент."""

    last_name = models.CharField("Фамилия", max_length=150)
    first_name = models.CharField("Имя", max_length=150)
    phone = models.CharField("Телефон", max_length=32)
    email = models.EmailField("Email")
    advertisement = models.ForeignKey(
        Advertisement,
        on_delete=models.PROTECT,
        related_name="leads",
        verbose_name="Рекламная кампания",
    )

    class Meta:
        """Метаданные модели потенциального клиента."""

        ordering = ["last_name", "first_name"]
        verbose_name = "Потенциальный клиент"
        verbose_name_plural = "Потенциальные клиенты"

    def __str__(self) -> str:  # pylint: disable=invalid-str-returned
        return f"{self.last_name} {self.first_name}"
