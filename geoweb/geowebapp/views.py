# Create your views here.
from django.shortcuts import render

from django.utils.safestring import SafeString
from django.utils.safestring import mark_safe
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse
from django.views.generic import TemplateView
import uuid

from pyproj import CRS, Transformer
from shapely.wkt import loads as load_wkt
#from shapely.ops import transform
from shapely.geometry import Point

import requests
import folium
from folium.map import Marker, Template

import json

from .models import SamplingFeatures, TimeSeriesResults, \
    TimeSeriesResultValues, Results, CV_SamplingFeatureGeoType, CV_SamplingFeatureType
from .serializers import SamplingFeaturesSerializers

from .utils import get_client_ip

def map_view(request):
    geos = []
    features = []
    srid = 3857
    for feature in SamplingFeatures.objects.all().order_by('samplingfeatureid')[:]:
        if feature.featuregeometry.srid != srid:
            srid = feature.featuregeometry.srid
        geos.append({"type": "Feature",
                     "properties": {"name": feature.samplingfeaturename},
                     "geometry": {
                         "type": str(type(feature.featuregeometry).__name__),
                         "coordinates": list(feature.featuregeometry.coords)
                     }
                     }
                    )
        features.append(feature.samplingfeaturename)
    geometries = {
        "type": "FeatureCollection",
        "crs": {
            "type": "name",
            "properties": {
                "name": "urn:ogc:def:crs:EPSG::{0}".format(srid)
            }
        },
        "features": geos
    }
    with open('data.json', 'w') as fp:
        fp.write(json.dumps(geometries))
    return render(request, "home_detail.html", {"geojson_data": mark_safe(json.dumps(geometries)),
                                                "features": features
                                                })


@method_decorator(ensure_csrf_cookie, name='dispatch')
class MainView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        figure = folium.Figure()
        t = Transformer.from_crs(3857, 4326)

        # Create a FeatureGroup layer with sensor elements as a single layer
        sensors_fg = folium.FeatureGroup()
        # Create a FeatureGroup layer with field elements as a single layer
        champs_fg = folium.FeatureGroup()
        parcelles_fg = folium.FeatureGroup()
        fermes_fg = folium.FeatureGroup()
        user_location_fg = folium.FeatureGroup()

        all_features = SamplingFeatures.objects.all()
        map_center = all_features.first().featuregeometry.centroid

        sensors = all_features.filter(samplingfeaturecode__istartswith='CAF')
        fermes = all_features.filter(samplingfeaturecode='CookAgronomyFarm')
        champs = all_features.filter(samplingfeaturecode__istartswith='Field')
        parcelles = all_features.filter(
            samplingfeaturecode__istartswith='Parcel')
        user_locations = all_features.filter(
            samplingfeaturecode__istartswith='User_')
        # Make the folium map
        _map = folium.Map(
            location=t.transform(map_center.x, map_center.y),
            zoom_start=17,
            tiles='OpenStreetMap',
        )
        _map._name = "map"
        _map._id = "000"

        _map.add_to(figure)

        for sensor in sensors:  # sensor.objects.all()
            coords = sensor.featuregeometry.coords
            sensors_fg.add_child(folium.Marker(
                location=list(t.transform(coords[0], coords[1])),
                popup=sensor.samplingfeaturename,
                tooltip=sensor.samplingfeaturedescription,
                icon=folium.Icon(icon='fa-sensor', prefix='fa')
            )
            )

        for user_location in user_locations:  # sensor.objects.all()
            coords = user_location.featuregeometry.coords
            # print('coord', coords)
            user_location_fg.add_child(folium.Marker(
                location=list(t.transform(coords[0], coords[1])),
                popup=user_location.samplingfeaturename,
                tooltip=user_location.samplingfeaturedescription,
                icon=folium.Icon(icon='fa-anchor', prefix='fa')
            )
            )

        for parcelle in parcelles:  # sensor.objects.all()
            wkt = load_wkt(parcelle.featuregeometrywkt)

            # Handle both Polygon and MultiPolygon
            if wkt.geom_type == 'MultiPolygon':
                for poly in wkt.geoms:
                    parcelles_fg.add_child(folium.Polygon(
                        locations=list(t.transform(coord[0], coord[1])
                                       for coord in poly.exterior.coords),
                        smooth_factor=4,
                        no_clip=True,
                        popup=parcelle.samplingfeaturename,
                        tooltip=parcelle.samplingfeaturedescription,
                        icon=folium.Icon(icon='fa-flag', prefix='fa')
                    ))
            else:
                parcelles_fg.add_child(folium.Polygon(
                    locations=list(t.transform(coord[0], coord[1])
                                   for coord in wkt.exterior.coords),
                    smooth_factor=4,
                    no_clip=True,
                    popup=parcelle.samplingfeaturename,
                    tooltip=parcelle.samplingfeaturedescription,
                    icon=folium.Icon(icon='fa-flag', prefix='fa')
                ))

        for champ in champs:  # sensor.objects.all()
            wkt = load_wkt(champ.featuregeometrywkt)

            # Handle both Polygon and MultiPolygon
            if wkt.geom_type == 'MultiPolygon':
                for poly in wkt.geoms:
                    champs_fg.add_child(folium.Polygon(
                        locations=list(t.transform(coord[0], coord[1])
                                       for coord in poly.exterior.coords),
                        smooth_factor=4,
                        no_clip=True,
                        popup=champ.samplingfeaturename,
                        tooltip=champ.samplingfeaturedescription,
                        icon=folium.Icon(icon='fa-flag', prefix='fa')
                    ))
            else:
                champs_fg.add_child(folium.Polygon(
                    locations=list(t.transform(coord[0], coord[1])
                                   for coord in wkt.exterior.coords),
                    smooth_factor=4,
                    no_clip=True,
                    popup=champ.samplingfeaturename,
                    tooltip=champ.samplingfeaturedescription,
                    icon=folium.Icon(icon='fa-flag', prefix='fa')
                ))

        for ferme in fermes:  # sensor.objects.all()
            wkt = load_wkt(ferme.featuregeometrywkt)

            # Handle both Polygon and MultiPolygon
            if wkt.geom_type == 'MultiPolygon':
                for poly in wkt.geoms:
                    fermes_fg.add_child(folium.Polygon(
                        locations=list(t.transform(coord[0], coord[1])
                                       for coord in poly.exterior.coords),
                        smooth_factor=4,
                        no_clip=True,
                        popup=ferme.samplingfeaturename,
                        tooltip=ferme.samplingfeaturedescription,
                        icon=folium.Icon(icon='fa-flag', prefix='fa')
                    ))
            else:
                fermes_fg.add_child(folium.Polygon(
                    locations=list(t.transform(coord[0], coord[1])
                                   for coord in wkt.exterior.coords),
                    smooth_factor=4,
                    no_clip=True,
                    popup=ferme.samplingfeaturename,
                    tooltip=ferme.samplingfeaturedescription,
                    icon=folium.Icon(icon='fa-flag', prefix='fa')
                ))
                smooth_factor = 4,
                no_clip = True,
                popup = ferme.samplingfeaturename,
                tooltip = ferme.samplingfeaturedescription,
                icon = folium.Icon(icon='fa-flag', prefix='fa')

        # Modify Marker template to include the onClick event
        click_template = """{% macro script(this, kwargs) %}
                            var {{ this.get_name() }} = L.marker(
                                {{ this.location|tojson }},
                                {{ this.options|tojson }}
                            ).addTo({{ this._parent.get_name() }}).on('click', getSensor);
                           {% endmacro %}
                        """
        # Change template to custom template
        Marker._template = Template(click_template)
        _ = _map._repr_html_()
        event_handler = folium.JavascriptLink('./static/js/eventhandler.js')

        plotly_js = "https://cdn.plot.ly/plotly-3.0.1.min.js"
        _map.get_root().html.add_child(folium.JavascriptLink(plotly_js))
        _map.get_root().html.add_child(event_handler)

        _map.add_child(user_location_fg)
        _map.add_child(sensors_fg)
        _map.add_child(parcelles_fg)
        _map.add_child(champs_fg)
        _map.add_child(fermes_fg)

        # LayerControl object to control display of layers, must be added last to the map.
        _map.add_child(folium.LayerControl())

        sensors_json = JsonResponse(
            SamplingFeaturesSerializers(sensors, many=True).data).content
        return {"map": figure._repr_html_(), 'title': 'Cook Agronomy Farm', 'sensors': sensors_json}
    

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

