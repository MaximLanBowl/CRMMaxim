from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.views.generic.edit import ModelFormMixin

from .forms import ServiceForm
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
    fields = '__all__'
    template_name = 'leads/leads-create.html'
    permission_required = 'clients.create_user'
    success_url = reverse_lazy("clients:list")


    def test_func(self):
        return self.request.user.is_superuser


class ClientsListView(ListView):
    model = Client
    template_name = 'leads/leads-list.html'
    form_class = ServiceForm
