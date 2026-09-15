from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import ProductForm
from .models import Product


class ProductListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """Список услуг."""

    model = Product
    template_name = "products/products-list.html"
    context_object_name = "products"
    permission_required = "products.view_product"


class ProductDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    """Детальная информация об услуге."""

    model = Product
    template_name = "products/products-detail.html"
    permission_required = "products.view_product"


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Создание услуги."""

    model = Product
    form_class = ProductForm
    template_name = "products/products-create.html"
    permission_required = "products.add_product"
    success_url = reverse_lazy("products:list")


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Редактирование услуги."""

    model = Product
    form_class = ProductForm
    template_name = "products/products-edit.html"
    permission_required = "products.change_product"
    success_url = reverse_lazy("products:list")


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Удаление услуги."""

    model = Product
    template_name = "products/products-delete.html"
    permission_required = "products.delete_product"
    success_url = reverse_lazy("products:list")
