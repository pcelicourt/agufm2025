from django.contrib.gis.db import models


class NonSpatialCities(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    population = models.IntegerField()
    geolocation = models.CharField(max_length=200)  # why not a geometry field here?
    province = models.CharField(max_length=200)

    class Meta:
        app_label = 'geowebapis'
        managed = True
        

class Countries(models.Model):
    country_id = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=128, unique=True)
    country_name_eng = models.CharField(max_length=128, unique=True)
    country_code = models.CharField(max_length=8, unique=True)
    # GeoDjango-specific: a geometry field (PolygonField)
    geom = models.PolygonField()

    class Meta:
        app_label = 'geowebapis'
        managed = True

class Cities(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=128, unique=True)
    location = models.PointField()
    country_id = models.ForeignKey('Countries', to_field='country_id', on_delete=models.CASCADE)

    class Meta:
        app_label = 'geowebapis'
        managed = True


