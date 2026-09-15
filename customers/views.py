from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from crm_system.mixins import ProtectedDeleteMixin

from .forms import CustomerForm
from .models import Customer


class CustomerListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """Список активных клиентов."""

    model = Customer
    template_name = "customers/customers-list.html"
    context_object_name = "customers"
    permission_required = "customers.view_customer"


class CustomerDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    """Детальная информация об активном клиенте."""

    model = Customer
    template_name = "customers/customers-detail.html"
    permission_required = "customers.view_customer"


class CustomerCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Создание активного клиента из потенциального."""

    model = Customer
    form_class = CustomerForm
    template_name = "customers/customers-create.html"
    permission_required = "customers.add_customer"
    success_url = reverse_lazy("customers:list")

    def get_initial(self) -> dict[str, Any]:
        initial = super().get_initial()
        lead_id = self.request.GET.get("lead")
        if lead_id:
            initial["lead"] = lead_id
        return initial


class CustomerUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Редактирование активного клиента."""

    model = Customer
    form_class = CustomerForm
    template_name = "customers/customers-edit.html"
    permission_required = "customers.change_customer"
    success_url = reverse_lazy("customers:list")


class CustomerDeleteView(
    LoginRequiredMixin, PermissionRequiredMixin, ProtectedDeleteMixin, DeleteView
):
    """Удаление активного клиента."""

    model = Customer
    template_name = "customers/customers-delete.html"
    permission_required = "customers.delete_customer"
    success_url = reverse_lazy("customers:list")
