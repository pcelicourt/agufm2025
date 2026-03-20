from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from geowebapp.models import SamplingFeatures
from .serializer import SamplingFeatureSerializers


# Create your views here.
@api_view(['GET'])
def get_full_metadata(request):
    all_features = SamplingFeatures.objects.all()
    serializer = SamplingFeatureSerializers(all_features, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_farm_metadata(request):
    ferme = SamplingFeatures.objects.filter(
        samplingfeaturecode='CookAgronomyFarm')
    serializer = SamplingFeatureSerializers(ferme, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_sensors_metadata(request):
    sensors = SamplingFeatures.objects.filter(
        samplingfeaturecode__istartswith='CAF')
    serializer = SamplingFeatureSerializers(sensors, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_single_sensor_metadata(request, sensorid):
    if 'CAF' in sensorid:
        sensors = SamplingFeatures.objects.filter(samplingfeaturecode=sensorid)
        serializer = SamplingFeatureSerializers(sensors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({}, status=status.HTTP_200_OK)
