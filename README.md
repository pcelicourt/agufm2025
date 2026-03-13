# Tutorial \#4 for the American Geophysical Union Fall Meeting 2025
This tutorial will help you create both a front-end and back-end api in Django.

## 1. Connect to your existing account

- [GitHub Sign in](https://github.com/login?)

## 2. Access the workshop GitHub repository

Click the following link to open the workshop repository: [AGUFM 2025 Workshop GitHub Repo](https://github.com/pcelicourt/agufm2025/tree/api-frontend).

## 3. Create a codespace from the branch api-frontend

With the branch api-frontend selected in the agufm2025 repo, click : (a) the blue button labelled **<> Code**, (b) tab Codespaces, then (c) **+** sign to create a codespace from the branch.

## 4. Continue the Django WebGIS Application development
In the Codespace terminal, run the following commands.

### 4.1. Verify Python and Django versions in the Codespace terminal

```bash
source .venv/bin/activate
python --version
pip install -r requirements.txt
python -m django --version
```

### 4.3. Change into the `geoweb` directory
Note that you must execute the following commands containing 'python -m manage ...' or 'python manage.py ...' within the geoweb folder.

```bash
cd geoweb
```

## 4.4 Check and run migrations 

In the Codespace terminal, you can check the content of the migrations files with the geoweb/geowebapp/migrations/ folder. Then, run the following command in the terminal.

```bash
python manage.py migrate
python manage.py startapp geowebapis
```

### 4.5 Replace the `INSTALLED_APPS` variable with:

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
   "django.contrib.staticfiles",
    "django.contrib.gis",
    "geowebapp",
    "geowebapis",
    "rest_framework",
    "rest_framework_gis",
]
```

## 5: Test how the ModelSerializer Class work in the console with the following commands
```bash
python manage.py shell
from geowebapis.models import NonSpatialCities
from geowebapis.serializer import NonSpatialCitiesModelSerializer
montreal = NonSpatialCities(1, 'Montreal', 'Canada', 1.8, (45.50884, -73.58781), 'Quebec')
serializer = NonSpatialCitiesModelSerializer(montreal)
serializer.data
exit()
```

## 6. Migrations command
In the Codespace terminal, run the following command to create the migrations for the models module of the geowebapis app :
```bash
python manage.py makemigrations geowebapis
python manage.py migrate geowebapis
python manage.py makemigrations --empty geowebapis
```

## 7. Populate the new migration file created. It starts with 0002_auto....

```bash
from django.db import migrations

import os
import pandas as pd

import geopandas as gpd
from shapely.geometry import Point, LineString, Polygon
from django.contrib.gis.geos import fromstr

def read_countries_data(country_code):
    file_path = f"./geowebapis/static/data/json/{country_code}.json"
    full_file_path = os.path.abspath(file_path)
    country_gdf = gpd.read_file(full_file_path)
    country_gdf['eng_name'] = country_gdf['name']
    country_gdf['code'] = f"{country_code}"
    return country_gdf

def read_cities_data_as_gdf(country_code=None):
    file_path = './geowebapis/static/data/csv/canadacities.csv'
    full_file_path = os.path.abspath(file_path)
    cities = pd.read_csv(full_file_path, delimiter=',')
    cities["Coordinates"] = list(zip(cities.lng, cities.lat)) 
    cities["Coordinates"] = cities["Coordinates"].apply(Point)
    cities_gdf = gpd.GeoDataFrame(cities, geometry="Coordinates")
    if country_code:
        cities_gdf = cities_gdf[cities_gdf.province_id == f"{country_code}"].sample(50).reset_index().drop('index', axis='columns')   
    cities_gdf = cities_gdf[['id', 'City', 'Coordinates', 'province_id']]
    return cities_gdf

def load_data_to_db(apps, schema_editor):
    Countries = apps.get_model('geowebapis', 'Countries')
    country_gdf = read_countries_data('SK')
    for index, country in country_gdf.iterrows():
        country_name = country['name']
        country_name_eng = country['eng_name']
        country_code = country['code']
        country_geometry = fromstr(str(country['geometry']), srid=4326)
        Countries(country_name=country_name, country_name_eng=country_name_eng,
                country_code=country_code, geom=country_geometry).save()

    Cities = apps.get_model('geowebapis', 'Cities')
    cities_gdf = read_cities_data_as_gdf('SK')
    #provinces_data = Provinces.objects.all().values()
    #provinces_data = Provinces.objects.values_list('country_code', 'country_id')
    for index, city in cities_gdf.iterrows():
        city_name = city['City']
        city_geometry = fromstr(str(city['Coordinates']), srid=4326)
        province_id = city['province_id']
        province_id = Countries.objects.filter(country_code=province_id).first()
        Cities(city_name=city_name, location=city_geometry, country_id=province_id).save()

class Migration(migrations.Migration):

    dependencies = [
        ('geowebapis', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_data_to_db)
    ]
```
## 8: load the data into the DB
```bash
python manage.py migrate geowebapis
```

## 9: Commands to execute in the CodesSpaces Terminal
```bash
python manage.py shell
from geowebapis.models import Cities
from geowebapis.serializer import CitiesSerializers
from django.http import JsonResponse
cities = Cities.objects.all()[:20]
serialized_cities = CitiesSerializers(cities, many=True)
serialized_cities.data
print(JsonResponse(serialized_cities.data).content)
exit()
```