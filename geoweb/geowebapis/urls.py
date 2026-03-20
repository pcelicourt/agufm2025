from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.get_full_metadata, name='full_metadata'),
    path('farm/', views.get_farm_metadata, name='farm_metadata'),
    path('farm/sensors/', views.get_sensors_metadata, name='sensors_metadata'),
    path('farm/sensors/sensor/<str:sensorid>/',
         views.get_single_sensor_metadata, name='sensor'),
]
