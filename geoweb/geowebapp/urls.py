from django.urls import path, include
from . import views

urlpatterns = [
    path('staticmap/', views.map_view, name='map_view'),
    path('farm/', views.MainView.as_view(), name='farm'),
    path('farm/sensors/sensor', views.map_view, name='sensor'),
]