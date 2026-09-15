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

from .forms import LeadForm
from .models import Lead


class LeadListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """Список потенциальных клиентов."""

    model = Lead
    template_name = "leads/leads-list.html"
    context_object_name = "leads"
    permission_required = "leads.view_lead"


class LeadDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    """Детальная информация о потенциальном клиенте."""

    model = Lead
    template_name = "leads/leads-detail.html"
    permission_required = "leads.view_lead"


class LeadCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Создание потенциального клиента."""

    model = Lead
    form_class = LeadForm
    template_name = "leads/leads-create.html"
    permission_required = "leads.add_lead"
    success_url = reverse_lazy("leads:list")


class LeadUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Редактирование потенциального клиента."""

    model = Lead
    form_class = LeadForm
    template_name = "leads/leads-edit.html"
    permission_required = "leads.change_lead"
    success_url = reverse_lazy("leads:list")


class LeadDeleteView(
    LoginRequiredMixin, PermissionRequiredMixin, ProtectedDeleteMixin, DeleteView
):
    """Удаление потенциального клиента."""

    model = Lead
    template_name = "leads/leads-delete.html"
    permission_required = "leads.delete_lead"
    success_url = reverse_lazy("leads:list")
