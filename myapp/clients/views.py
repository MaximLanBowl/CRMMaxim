from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.views.generic.edit import ModelFormMixin, UpdateView, DeleteView

from .forms import ServiceForm, ClientsForm
from .models import Client


# Create your views here.

def LoginView(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/admin/')
        return render(request, 'registration/login.html')

    username = request.POST["username"]
    password = request.POST["password"]

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/admin/')
    else:
        return render(request, 'registration/login.html', {"error": 'Invalid login'})


class ClientsCreateView(CreateView, ModelFormMixin):
    model = Client
    fields = 'username', 'email'
    template_name = 'leads/leads-create.html'
    permission_required = 'clients.create_user'
    success_url = reverse_lazy("clients:list")


class ClientsListView(ListView):
    model = User
    template_name = 'leads/leads-list.html'
    form_class = ClientsForm


class ClientsEditView(UpdateView):
    model = Client
    template_name = 'leads/leads-edit.html'


class ClientsDeleteView(DeleteView):
    model = Client
