from django.contrib import admin

from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """Административный интерфейс для активных клиентов."""

    list_display = ("lead", "contract")
    search_fields = ("lead__last_name", "lead__first_name")
