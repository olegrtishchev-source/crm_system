from django import forms

from .models import Lead


class LeadForm(forms.ModelForm):
    """Форма создания и редактирования потенциального клиента."""

    class Meta:
        """Поля формы потенциального клиента."""

        model = Lead
        fields = ["last_name", "first_name", "phone", "email", "advertisement"]
