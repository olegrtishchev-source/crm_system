"""Общие fixtures для тестов CRM: тестовые объекты и авторизованные клиенты."""

import datetime
from typing import Callable, Optional

import pytest
from django.contrib.auth.models import AbstractUser, Group
from django.core.files.uploadedfile import SimpleUploadedFile

from advertisements.models import Advertisement
from contracts.models import Contract
from customers.models import Customer
from leads.models import Lead
from products.models import Product


@pytest.fixture(autouse=True)
def _media_root(settings, tmp_path) -> None:
    """Файлы контрактов при тестах пишутся во временную папку, а не в media/."""
    settings.MEDIA_ROOT = tmp_path


@pytest.fixture
def product(db) -> Product:  # pylint: disable=unused-argument
    """Тестовая услуга."""
    return Product.objects.create(name="Разработка сайта", cost=50000)


@pytest.fixture
def advertisement(product: Product) -> Advertisement:  # pylint: disable=redefined-outer-name
    """Тестовая рекламная кампания."""
    return Advertisement.objects.create(
        name="Продвижение услуг по разработке сайта",
        product=product,
        channel="Яндекс.Директ",
        budget=10000,
    )


@pytest.fixture
def lead(advertisement: Advertisement) -> Lead:  # pylint: disable=redefined-outer-name
    """Тестовый потенциальный клиент."""
    return Lead.objects.create(
        last_name="Иванов",
        first_name="Иван",
        phone="+79990000000",
        email="ivanov@example.com",
        advertisement=advertisement,
    )


@pytest.fixture
def contract(product: Product) -> Contract:  # pylint: disable=redefined-outer-name
    """Тестовый контракт."""
    return Contract.objects.create(
        name="Договор №1",
        product=product,
        document=SimpleUploadedFile("contract.txt", b"test-document"),
        start_date=datetime.date(2026, 1, 1),
        end_date=datetime.date(2026, 12, 31),
        cost=100000,
    )


@pytest.fixture
def customer(lead: Lead, contract: Contract) -> Customer:  # pylint: disable=redefined-outer-name
    """Тестовый активный клиент — лид, переведённый по контракту."""
    return Customer.objects.create(lead=lead, contract=contract)


@pytest.fixture
def make_user(django_user_model) -> Callable[..., AbstractUser]:
    """Фабрика тестовых пользователей, опционально с ролью (группой)."""

    def _make_user(
        *, username: str = "tester", group_name: Optional[str] = None
    ) -> AbstractUser:
        user = django_user_model.objects.create_user(
            username=username, password="test-pass-12345"
        )
        if group_name:
            user.groups.add(Group.objects.get(name=group_name))
        return user

    return _make_user
