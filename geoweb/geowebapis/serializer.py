from rest_framework_gis import serializers
from geowebapis.models import NonSpatialCities, Countries, Cities


class NonSpatialCitiesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = NonSpatialCities
        fields = ['city_id', 'city_name', 'country', 'population', 'geolocation', 'province']


class CitiesSerializers(serializers.GeoFeatureModelSerializer):
    """ A class to serialize locations as GeoJSON compatible data """

    class Meta:
        app_label  = 'geowebapis'
        model = Cities
        geo_field = "geom"
        fields = ('city_id', 'city_name', 'country_id_id')