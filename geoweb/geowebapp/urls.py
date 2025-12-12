from django.urls import path, include
from .views import map_view, MainView, store_user_location, location_from_ip


urlpatterns = [
    path('staticmap/', map_view, name='map_view'),
    path('user-location/', store_user_location, name='user_location'),
    path('location-from-ip/', location_from_ip, name='location_from_ip'),
]