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

from .forms import ContractForm
from .models import Contract


class ContractListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """Список контрактов."""

    model = Contract
    template_name = "contracts/contracts-list.html"
    context_object_name = "contracts"
    permission_required = "contracts.view_contract"


class ContractDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    """Детальная информация о контракте."""

    model = Contract
    template_name = "contracts/contracts-detail.html"
    permission_required = "contracts.view_contract"


class ContractCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Создание контракта."""

    model = Contract
    form_class = ContractForm
    template_name = "contracts/contracts-create.html"
    permission_required = "contracts.add_contract"
    success_url = reverse_lazy("contracts:list")


class ContractUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Редактирование контракта."""

    model = Contract
    form_class = ContractForm
    template_name = "contracts/contracts-edit.html"
    permission_required = "contracts.change_contract"
    success_url = reverse_lazy("contracts:list")


class ContractDeleteView(
    LoginRequiredMixin, PermissionRequiredMixin, ProtectedDeleteMixin, DeleteView
):
    """Удаление контракта."""

    model = Contract
    template_name = "contracts/contracts-delete.html"
    permission_required = "contracts.delete_contract"
    success_url = reverse_lazy("contracts:list")
