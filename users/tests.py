"""Тесты для приложения users: дашборд и роли."""

import pytest
from django.contrib.auth.models import Group
from django.urls import reverse

from customers.models import Customer
from leads.models import Lead

ROLE_NAMES = ["Администратор", "Оператор", "Маркетолог", "Менеджер"]


@pytest.mark.django_db
def test_roles_created_by_migration() -> None:
    """Миграция users.0001_create_roles создаёт все четыре роли с правами."""
    assert Group.objects.filter(name__in=ROLE_NAMES).count() == len(ROLE_NAMES)

    marketer = Group.objects.get(name="Маркетолог")
    assert marketer.permissions.filter(
        content_type__app_label="products", codename="add_product"
    ).exists()
    assert marketer.permissions.filter(
        content_type__app_label="advertisements", codename="view_advertisement"
    ).exists()


@pytest.mark.django_db
def test_dashboard_requires_only_login(
    client,
    make_user,
    lead: Lead,  # pylint: disable=unused-argument
    customer: Customer,  # pylint: disable=unused-argument
) -> None:
    """Дашборд доступен любому авторизованному пользователю без привязки к роли."""
    user = make_user()
    client.force_login(user)

    response = client.get(reverse("users:index"))

    assert response.status_code == 200
    assert response.context["leads_count"] == 1
    assert response.context["customers_count"] == 1
