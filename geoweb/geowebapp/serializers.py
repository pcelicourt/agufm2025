from rest_framework_gis.serializers import GeoFeatureModelSerializer


from .models import SamplingFeatures

class SamplingFeaturesSerializers(GeoFeatureModelSerializer):
    """ A class to serialize locations as GeoJSON compatible data """

    class Meta:
        app_label  = 'agrogeoinfoapp'
        model = SamplingFeatures
        geo_field = "featuregeometry"
        fields = '__all__'