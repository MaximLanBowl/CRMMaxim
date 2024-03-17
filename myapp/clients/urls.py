from django.urls import path
from .views import (
    ClientsCreateView,
    ClientsListView,

)

app_name = "clients"

urlpatterns = [
    path('list/', ClientsListView.as_view(), name='list'),
    path('new/', ClientsCreateView.as_view(), name='create'),

]


