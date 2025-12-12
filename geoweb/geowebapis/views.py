from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
import uuid

import requests
from geowebapp.models import SamplingFeatures, TimeSeriesResults, \
    TimeSeriesResultValues, Results, CV_SamplingFeatureGeoType, CV_SamplingFeatureType
from shapely.geometry import Point
from pyproj import CRS, Transformer



