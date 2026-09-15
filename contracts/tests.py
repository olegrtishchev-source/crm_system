"""Тесты для приложения contracts."""

import pytest

from .models import Contract


@pytest.mark.django_db
def test_contract_str(contract: Contract) -> None:
    """__str__ модели возвращает название контракта."""
    assert str(contract) == contract.name
