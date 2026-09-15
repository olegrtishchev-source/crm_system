from django.contrib import admin

from .models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    """Административный интерфейс для потенциальных клиентов."""

    list_display = ("last_name", "first_name", "phone", "email", "advertisement")
    list_filter = ("advertisement",)
    search_fields = ("last_name", "first_name", "phone", "email")
