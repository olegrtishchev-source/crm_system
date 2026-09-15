from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Административный интерфейс для услуг."""

    list_display = ("name", "cost")
    search_fields = ("name",)
