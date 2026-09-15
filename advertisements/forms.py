from django import forms

from .models import Advertisement


class AdvertisementForm(forms.ModelForm):
    """Форма создания и редактирования рекламной кампании."""

    class Meta:
        """Поля формы рекламной кампании."""

        model = Advertisement
        fields = ["name", "product", "channel", "budget"]
