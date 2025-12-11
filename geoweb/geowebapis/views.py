from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
import uuid

import requests
from geowebapp.models import SamplingFeatures, TimeSeriesResults, \
    TimeSeriesResultValues, Results, CV_SamplingFeatureGeoType, CV_SamplingFeatureType
from shapely.geometry import Point
from pyproj import CRS, Transformer

from .utils import get_client_ip

userlocationfeaturegeotypecv = CV_SamplingFeatureGeoType.objects.filter(
    term='point').first()

sampling_feature_type_cv = CV_SamplingFeatureType.objects.filter(
    term="site").first()


@ensure_csrf_cookie
def store_user_location(request):
    if request.method == 'POST':
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        timestamp = request.POST.get('timestamp')
        print(latitude, longitude, timestamp)
        crs_transformer = Transformer.from_crs(4326, 3857, always_xy=True)
        longitude, latitude = crs_transformer.transform(
            float(longitude), float(latitude))
        point = Point(float(longitude), float(latitude))
        wkt = point.wkt
        print(wkt)
        # Save into the DB
        user_location = SamplingFeatures(
            samplingfeatureuuid=str(uuid.uuid4()),
            samplingfeaturename=f'User Location {timestamp}',
            samplingfeaturetypecv=sampling_feature_type_cv,
            samplingfeaturecode=f'User_{timestamp}',
            samplingfeaturedescription='User Location from Browser',
            featuregeometry=wkt,
            featuregeometrywkt=wkt,
            samplingfeaturegeotypecv=userlocationfeaturegeotypecv,
            elevation_m=-9999,
            # elevationdatumcv=elevation_datum_cv,
        )
        user_location.save()
        all_features = SamplingFeatures.objects.filter(
            samplingfeaturedescription='User Location from Browser')  # QuerySet
        last_feature = all_features[::-1][0]
        print("Last feature saved:", last_feature.featuregeometry)
        return JsonResponse({'status': 'success', 'latitude': latitude, 'longitude': longitude})
    elif request.method == 'GET':
        # Temporarily handle GET for debugging
        return JsonResponse({
            'status': 'error',
            'message': 'POST request expected but received GET',
            'method': request.method
        })

    return JsonResponse({'status': 'invalid request', 'method': request.method}, status=400)


def get_geolocation_data(ip_address):
    api_key = 'a61126b08a4c45528b8f60aa276a2671'
    url = f'https://ipgeolocation.abstractapi.com/v1/?api_key={api_key}&ip_address={ip_address}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            'city': data.get('city'),
            'region': data.get('region'),
            'country': data.get('country'),
            'latitude': data.get('latitude'),
            'longitude': data.get('longitude'),
        }

    return None


def location_from_ip(request):
    user_ip = get_client_ip(request)
    location_data = get_geolocation_data(user_ip)
    if location_data:
        # Store or personalize based on location_data
        return JsonResponse({'location': location_data})
    return JsonResponse({'error': 'Location not found'}, status=404)
