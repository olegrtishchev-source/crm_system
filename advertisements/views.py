from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Count, QuerySet, Sum
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from crm_system.mixins import ProtectedDeleteMixin

from .forms import AdvertisementForm
from .models import Advertisement


class AdvertisementListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """Список рекламных кампаний."""

    model = Advertisement
    template_name = "ads/ads-list.html"
    context_object_name = "ads"
    permission_required = "advertisements.view_advertisement"


class AdvertisementDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    """Детальная информация о рекламной кампании."""

    model = Advertisement
    template_name = "ads/ads-detail.html"
    permission_required = "advertisements.view_advertisement"


class AdvertisementCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Создание рекламной кампании."""

    model = Advertisement
    form_class = AdvertisementForm
    template_name = "ads/ads-create.html"
    permission_required = "advertisements.add_advertisement"
    success_url = reverse_lazy("advertisements:list")


class AdvertisementUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Редактирование рекламной кампании."""

    model = Advertisement
    form_class = AdvertisementForm
    template_name = "ads/ads-edit.html"
    permission_required = "advertisements.change_advertisement"
    success_url = reverse_lazy("advertisements:list")


class AdvertisementDeleteView(
    LoginRequiredMixin, PermissionRequiredMixin, ProtectedDeleteMixin, DeleteView
):
    """Удаление рекламной кампании."""

    model = Advertisement
    template_name = "ads/ads-delete.html"
    permission_required = "advertisements.delete_advertisement"
    success_url = reverse_lazy("advertisements:list")


class AdvertisementStatisticView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """Статистика эффективности рекламных кампаний: количество лидов и
    привлечённых активных клиентов, соотношение суммы контрактов к
    затратам на рекламу."""

    model = Advertisement
    template_name = "ads/ads-statistic.html"
    context_object_name = "ads"
    permission_required = "advertisements.view_advertisement"
    paginate_by = 20

    def get_queryset(self) -> QuerySet[Advertisement]:
        ads = Advertisement.objects.annotate(
            leads_count=Count("leads", distinct=True),
            customers_count=Count("leads__customer", distinct=True),
            contracts_cost=Sum("leads__customer__contract__cost"),
        )
        for ad in ads:
            contracts_cost = ad.contracts_cost  # type: ignore[attr-defined]
            ad.profit = (  # type: ignore[attr-defined]
                round(contracts_cost / ad.budget, 2)
                if contracts_cost and ad.budget
                else None
            )
        return ads
