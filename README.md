# agufm2025
Template for Geoinformatics workshop at AGU Fall Meeting 2025

Run the following commands to create a Django WebGIS Application in your terminal

$ source .venv/bin/activate

$ python --version

$ python -m django --version

django-admin startproject geoweb

cd geoweb

python manage.py startapp geowebapp

#settings.py
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
 "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
   "django.contrib.staticfiles",
    "django.contrib.gis", #explanation here
    "geowebapp",
]


DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": os.getenv("POSTGRES_DB", "mydb"),
        "USER": os.getenv("POSTGRES_USER", "postgres"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD", "postgres"),
        "HOST": os.getenv("POSTGRES_HOST", "localhost"),  # or "db" when using Compose
        "PORT": os.getenv("POSTGRES_PORT", "5432"),
    }
}

$ python manage.py migrate
$ python manage.py runserver