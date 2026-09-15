"""Тесты для приложения customers."""

import pytest

from .forms import CustomerForm
from .models import Customer


@pytest.mark.django_db
def test_customer_str(customer: Customer) -> None:
    """__str__ модели совпадает со строковым представлением лида."""
    assert str(customer) == str(customer.lead)


@pytest.mark.django_db
def test_form_excludes_already_converted_lead(customer: Customer) -> None:
    """Лид, уже ставший активным клиентом, не должен предлагаться повторно."""
    form = CustomerForm()

    assert customer.lead not in form.fields["lead"].queryset  # type: ignore[attr-defined]


@pytest.mark.django_db
def test_form_keeps_current_lead_on_edit(customer: Customer) -> None:
    """При редактировании существующего клиента его текущий лид остаётся в списке."""
    form = CustomerForm(instance=customer)

    assert customer.lead in form.fields["lead"].queryset  # type: ignore[attr-defined]
