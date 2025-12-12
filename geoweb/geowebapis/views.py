from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
import uuid

import requests
from geowebapp.models import SamplingFeatures, TimeSeriesResults, \
    TimeSeriesResultValues, Results, FeatureActions, CV_SamplingFeatureGeoType, CV_SamplingFeatureType
from shapely.geometry import Point
from pyproj import CRS, Transformer

from geowebapp.serializers import SamplingFeaturesSerializers


@ensure_csrf_cookie
def sensor_data(request):
    if request.method == 'POST':
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        sensor_code = request.POST.get('sensor_name')
    elif request.method == 'GET':
        latitude = request.GET.get('latitude')
        longitude = request.GET.get('longitude')
        sensor_code = request.GET.get('sensor_name')
            
    print(latitude, longitude, sensor_code)
    sampling_feature = SamplingFeatures.objects.filter(
        samplingfeaturecode=f"{sensor_code}").first()

    featureaction = FeatureActions.objects.filter(
        samplingfeatureid=sampling_feature).first()

    results = Results.objects.filter(
        featureactionid=featureaction).first()

    timeseries_results = TimeSeriesResults.objects.filter(
        resultid=results).first()

    timeseries_values = TimeSeriesResultValues.objects.filter(
        resultid=timeseries_results).all().order_by('-valuedatetime')[:5]

    # Convert query results to JSON-serializable format
    values_list = []
    for value in timeseries_values:
        values_list.append({
            'value': float(value.datavalue),
            'datetime': value.valuedatetime.isoformat() if value.valuedatetime else None
        })
        print(f"Value: {value.datavalue}, DateTime: {value.valuedatetime}")

    variable = results.variableid.variablenamecv.term
    print(f"Variable: {variable}")
    unit = results.unitsid.unitsname
    print(f"Unit: {unit}")

    # Return structured JSON data
    return JsonResponse({
        'status': 'success',
        'sensor_code': sensor_code,
        'variable': variable,
        'unit': unit,
        'data': values_list,
        'count': len(values_list)
    })

