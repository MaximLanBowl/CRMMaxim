from django.urls import path

app_name = 'uslugi'

from .views import (
    ProductCreateView,
    ProductListView, ProductDeleteView, ProductEditView,
)

urlpatterns = [
    path('new/', ProductCreateView.as_view(), name='create'),
    path('', ProductListView.as_view(), name='products_list'),
    path('<int:pk>/edit/', ProductEditView.as_view(), name='edit_product'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='delete_product')

]
