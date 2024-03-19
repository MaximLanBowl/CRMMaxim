from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic.edit import ModelFormMixin, UpdateView, DeleteView

from .forms import ProductForm
from .models import Product


class ProductCreateView(CreateView):
    template_name = 'products/products-create.html'
    queryset = Product.objects.filter(name=True)
    permission_required = "products.change_product"
    fields = "name", "price", "description"
    success_url = reverse_lazy("uslugi:products")


class ProductListView(ListView):
    model = Product
    template_name = 'products/products-list.html'
    context_object_name = "products"
    queryset = Product.objects.filter(name=True)


class ProductEditView(UpdateView):
    template_name = 'products/products-edit.html'
    form_class = ProductForm
    model = Product

    def get_success_url(self):
        return reverse(
            "uslugi:detail",
            kwargs={"pk": self.object.pk},
        )


class ProductDetailsView(DetailView):
    model = Product
    template_name = 'products/products-detail.html'
    context_object_name = "product"


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/products-delete.html'
    success_url = reverse_lazy("uslugi:product_list")