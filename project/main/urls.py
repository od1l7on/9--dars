from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('brand/<int:brand_id>/', views.brand_filter, name='brand_filter'),
    path('car/<int:car_id>/', views.car_detail, name='car_detail'),
    path('add-car/', views.add_car, name='add_car'),
    path('add-brand/', views.add_brand, name='add_brand'),
]