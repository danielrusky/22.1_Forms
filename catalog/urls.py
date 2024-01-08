from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ContactsView, ProductListView, ProductDetailView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView, CategoryCreateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contacts/',ContactsView.as_view(), name='contact'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('create_product/', ProductCreateView.as_view(), name='create_product'),
    path('view/<int:pk>', ProductDetailView.as_view(), name='view_product'),
    path('edit/<int:pk>', ProductUpdateView.as_view(), name='edit_product'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete_product'),
    path('create_category/', CategoryCreateView.as_view(), name='create_category'),
]