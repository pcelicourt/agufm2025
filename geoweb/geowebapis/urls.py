from django.urls import path

from .views import sensor_data, sampling_features


urlpatterns = [
    path('sensor/', sensor_data, name='sensor'),
    path('samplingfeatures/', sampling_features, name='samplingfeatures'),    
] 