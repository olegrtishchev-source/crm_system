from django.db import models

from contracts.models import Contract
from leads.models import Lead


class Customer(models.Model):
    """Активный клиент — создаётся из потенциального при заключении контракта."""

    lead = models.OneToOneField(
        Lead,
        on_delete=models.PROTECT,
        related_name="customer",
        verbose_name="Потенциальный клиент",
    )
    contract = models.ForeignKey(
        Contract,
        on_delete=models.PROTECT,
        related_name="customers",
        verbose_name="Контракт",
    )

    class Meta:
        """Метаданные модели активного клиента."""

        ordering = ["lead__last_name", "lead__first_name"]
        verbose_name = "Активный клиент"
        verbose_name_plural = "Активные клиенты"

    def __str__(self) -> str:  # pylint: disable=invalid-str-returned
        return str(self.lead)
