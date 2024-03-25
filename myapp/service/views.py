from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import Service
from .forms import ServiceForm


class ServiceListView(ListView):
    model = Service
    template_name = 'service/products-list.html'


class ServiceDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'service.view_service'
    queryset = (
        Service.objects
        .select_related("name")
        .prefetch_related("description")
    )


class ServiceCreateView(CreateView):
    model = Service
    template_name = 'service/products-create.html'
    fields = 'name', 'description', 'price'
    success_url = reverse_lazy("service:list")


class ServiceEditView(UpdateView):
    model = Service
