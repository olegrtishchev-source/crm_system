from django import forms
from django.db.models import Q

from leads.models import Lead

from .models import Customer


class CustomerForm(forms.ModelForm):
    """Форма создания и редактирования активного клиента."""

    class Meta:
        """Поля формы активного клиента."""

        model = Customer
        fields = ["lead", "contract"]

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        available_leads = Q(customer__isnull=True)
        if self.instance.pk:
            available_leads |= Q(pk=self.instance.lead_id)
        self.fields["lead"].queryset = Lead.objects.filter(  # type: ignore[attr-defined]
            available_leads
        )
