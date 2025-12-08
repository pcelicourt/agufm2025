# Tutorial for the American Geophysical Union Fall Meeting 2025

# Following the setup of the agufm25 template in CodeSpaces, run the following commands to create a Django WebGIS Application in your terminal

# CodeSpaces Terminal
$ source .venv/bin/activate

$ python --version

$ python -m django --version

# Still in the terminal, run the following commands to create a Django Project with name geoweb
$ django-admin startproject geoweb

# Change to the newly created directory geoweb
$ cd geoweb

# Still in the terminal, run the following commands to create a Django App with name geowebapp
$ python manage.py startapp geowebapp

# In the settings.py file within the geoweb folder, add the following codes
import os

from dotenv import load_dotenv

load_dotenv(os.path.join(BASE_DIR, ".env"))

# Replace the variable INSTALLED_APPS with the following value
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
   "django.contrib.staticfiles",
    "django.contrib.gis",
    "geowebapp",
]

# Replace the variable DATABASES with the following value
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

# CodeSpaces Terminal
$ python manage.py migrate
$ python manage.py runserver