from django.urls import path
from . import views
from .views import equipment_installation_create

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<str:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.product_create, name='product_create'),
    path('purchases/', views.purchase_list, name='purchase_list'),
    path('add-purchase/', views.purchase_create, name='purchase_create'),
    path('company/autocomplete/', views.company_autocomplete, name='company_autocomplete'),
     path('purchase/history/', views.purchase_history, name='purchase_history'),
     path('purchase-history-by-company/', views.purchase_history_by_company, name='purchase_history_by_company'),
      path('purchase-history-by-product-type/', views.purchase_history_by_product_type, name='purchase_history_by_product_type'),
      path('equipment-installation/create/', equipment_installation_create, name='equipment_installation_create'),
       path('equipment-installation/', views.equipment_installation_list, name='equipment_installation_list'),
    path('out-of-stock/', views.out_of_stock_products, name='out_of_stock_products')
]
