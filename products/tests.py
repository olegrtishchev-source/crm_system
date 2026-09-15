"""Тесты для приложения products."""

import pytest
from django.urls import reverse

from .models import Product


@pytest.mark.django_db
def test_product_str(product: Product) -> None:
    """__str__ модели возвращает название услуги."""
    assert str(product) == product.name


@pytest.mark.django_db
def test_list_requires_login(client) -> None:
    """Без авторизации — редирект на страницу входа."""
    response = client.get(reverse("products:list"))
    assert response.status_code == 302
    assert response.url.startswith("/accounts/login/")


@pytest.mark.django_db
def test_list_requires_permission(client, make_user) -> None:
    """Авторизован, но без права products.view_product — 403."""
    user = make_user()  # без роли — нет права products.view_product
    client.force_login(user)

    response = client.get(reverse("products:list"))

    assert response.status_code == 403


@pytest.mark.django_db
def test_list_with_permission(client, make_user, product: Product) -> None:
    """С правом (роль «Маркетолог») список услуг открывается."""
    user = make_user(group_name="Маркетолог")
    client.force_login(user)

    response = client.get(reverse("products:list"))

    assert response.status_code == 200
    assert product.name in response.content.decode()
