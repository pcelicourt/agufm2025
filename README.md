# Tutorial for the American Geophysical Union Fall Meeting 2025

## Create a github account
https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home


![alt text](https://github.com/pcelicourt/agufm2025/blob/ancillary/image.jpg?raw=true)

## Following the setup of the agufm25 template in CodeSpaces, run the following commands to create a Django WebGIS Application in your terminal

### CodeSpaces Terminal
$ source .venv/bin/activate

$ python --version

$ python -m django --version

### Still in the terminal, run the following commands to create a Django Project with name geoweb
$ django-admin startproject geoweb

### Change to the newly created directory geoweb
$ cd geoweb

### Still in the terminal, run the following commands to create a Django App with name geowebapp
$ python manage.py startapp geowebapp

### In the settings.py file within the geoweb folder, add the following codes
`
import os
from dotenv import load_dotenv
load_dotenv(os.path.join(BASE_DIR, ".env"))
from ctypes.util import find_library
`

### Replace the variable INSTALLED_APPS with the following value
`
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
`

### Replace the variable DATABASES with the following value
`
DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.spatialite",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
`
### Replace the variable TEMPLATES with the following value
`
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "geowebapp/static/templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
`
### At the end of the file, add the following variables
`
GDAL_LIBRARY_PATH = find_library("gdal")
GEOS_LIBRARY_PATH = find_library("geos_c")
SPATIALITE_LIBRARY_PATH = "mod_spatialite"
`

# In the CodeSpaces Terminal, execute the following commands
$ python manage.py migrate
$ python manage.py runserver
