from django import forms

from .models import Contract


class ContractForm(forms.ModelForm):
    """Форма создания и редактирования контракта."""

    class Meta:
        """Поля формы контракта."""

        model = Contract
        fields = ["name", "product", "document", "start_date", "end_date", "cost"]
        widgets = {
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "end_date": forms.DateInput(attrs={"type": "date"}),
        }
