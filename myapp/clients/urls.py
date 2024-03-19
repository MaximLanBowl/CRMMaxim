from django.urls import path
from .views import (
    ClientsCreateView,
    ClientsListView,
    ClientsDeleteView,

)

app_name = "clients"

urlpatterns = [
    path('', ClientsListView.as_view(), name='list'),
    path('new/', ClientsCreateView.as_view(), name='create'),
    path('<int:pk>/delete/', ClientsDeleteView.as_view(), name='delete')
]


