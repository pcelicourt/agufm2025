from django.urls import path
from . import views

urlpatterns = [
    path('user-location/', views.store_user_location, name='user_location'),
    path('location-from-ip/', views.location_from_ip, name='location_from_ip'),
] 