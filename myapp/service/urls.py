from django.urls import path

from .views import (
    ServiceListView,
    ServiceCreateView,
    ServiceEditView,
    ServiceDetailView,
)

app_name = 'service'

urlpatterns = [
    path('', ServiceListView.as_view(), name='list'),
    path('new/', ServiceCreateView.as_view(), name='create'),
]