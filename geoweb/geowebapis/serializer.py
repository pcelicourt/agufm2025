from rest_framework_gis import serializers

from geowebapis.models import NonSpatialCities, Countries, Cities
from geowebapp.models import SamplingFeatures


class NonSpatialCitiesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = NonSpatialCities
        fields = ['city_id', 'city_name', 'country',
                  'population', 'geolocation', 'province']


class CitiesSerializers(serializers.GeoFeatureModelSerializer):
    """ A class to serialize locations as GeoJSON compatible data """

    class Meta:
        app_label = 'geowebapis'
        model = Cities
        geo_field = "location"
        fields = ('city_id', 'city_name', 'country_id_id')


class SamplingFeatureSerializers(serializers.GeoFeatureModelSerializer):
    """ A class to serialize locations as GeoJSON compatible data """

    class Meta:
        app_label = 'geowebapis'
        model = SamplingFeatures
        geo_field = "featuregeometry"
        fields = '__all__'
