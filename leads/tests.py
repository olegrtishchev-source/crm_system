"""Тесты для приложения leads."""

import pytest
from django.urls import reverse

from customers.models import Customer

from .models import Lead


@pytest.mark.django_db
def test_lead_str(lead: Lead) -> None:
    """__str__ модели возвращает фамилию и имя."""
    assert str(lead) == f"{lead.last_name} {lead.first_name}"


@pytest.mark.django_db
def test_protected_delete_does_not_crash(
    client, make_user, lead: Lead, customer: Customer  # pylint: disable=unused-argument
) -> None:
    """Удаление лида, у которого уже есть активный клиент, не должно падать 500."""
    user = make_user(group_name="Оператор")
    client.force_login(user)

    response = client.post(reverse("leads:delete", args=[lead.pk]), follow=True)

    assert response.status_code == 200
    assert Lead.objects.filter(pk=lead.pk).exists()
    page_messages = list(response.context["messages"])
    assert any("нельзя удалить" in str(m).lower() for m in page_messages)
