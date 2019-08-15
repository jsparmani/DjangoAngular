from django.urls import path
from . import views

app_name = 'customers'

urlpatterns = [
    path('customers/', views.customer_list),
    path('customers/<int:pk>/', views.customer_detail),
    path('customers/age/<int:age>/', views.customer_list_age)
]
