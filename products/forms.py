from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    """Форма создания и редактирования услуги."""

    class Meta:
        """Поля формы услуги."""

        model = Product
        fields = ["name", "description", "cost"]
