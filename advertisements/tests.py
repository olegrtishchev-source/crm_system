"""Тесты для приложения advertisements."""

import pytest
from django.urls import reverse

from customers.models import Customer
from leads.models import Lead
from products.models import Product

from .models import Advertisement


@pytest.mark.django_db
def test_advertisement_str(advertisement: Advertisement) -> None:
    """__str__ модели возвращает название кампании."""
    assert str(advertisement) == advertisement.name


@pytest.mark.django_db
def test_statistic_counts_and_profit(
    client,
    make_user,
    advertisement: Advertisement,
    lead: Lead,  # pylint: disable=unused-argument
    customer: Customer,
) -> None:
    """Статистика считает лидов, клиентов и соотношение контрактов к бюджету."""
    user = make_user(group_name="Маркетолог")
    client.force_login(user)

    response = client.get(reverse("advertisements:statistic"))

    assert response.status_code == 200
    (ad,) = response.context["ads"]
    assert ad.pk == advertisement.pk
    assert ad.leads_count == 1
    assert ad.customers_count == 1
    assert ad.profit == round(customer.contract.cost / advertisement.budget, 2)


@pytest.mark.django_db
def test_statistic_zero_state(client, make_user, product: Product) -> None:
    """У кампании без откликов — нулевые счётчики и profit=None."""
    Advertisement.objects.create(
        name="Без откликов", product=product, channel="Радио", budget=5000
    )
    user = make_user(group_name="Маркетолог")
    client.force_login(user)

    response = client.get(reverse("advertisements:statistic"))

    (ad,) = response.context["ads"]
    assert ad.leads_count == 0
    assert ad.customers_count == 0
    assert ad.profit is None
