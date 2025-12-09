# Tutorial for the American Geophysical Union Fall Meeting 2025

## 1. Create a GitHub account or connect to an existing account

- [GitHub Signup](https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home)  
- [GitHub Sign in](https://github.com/login?)

## 2. Access the workshop GitHub repository

Click the following link to open the workshop repository: [AGUFM 2025 Workshop GitHub Repo](https://github.com/pcelicourt/agufm2025)

## 3. Open the repo in a Codespace

Open the repository in a Codespace as demonstrated in the image below:

![Launch CodeSpace](https://github.com/pcelicourt/aguassets/raw/main/images/codespacelaunching.png)

## 4. Codespace development environment

Your Codespace development environment should look similar to this:

![CodeSpace Terminal](https://github.com/pcelicourt/aguassets/raw/main/images/codespacesetup.png)

## 5. Creation of a Django WebGIS Application
In the Codespace terminal, run the following commands.

### 5.1. Verify Python and Django versions in the Codespace terminal

```bash
source .venv/bin/activate
python --version
pip install -r requirements.txt
python -m django --version
```

### 5.2. Create a Django project named `geoweb`

```bash
django-admin startproject geoweb
```

### 5.3. Change into the newly created `geoweb` directory

```bash
cd geoweb
```

### 5.4. Create a Django app named `geowebapp`

```bash
python manage.py startapp geowebapp
```

## 6. Update `settings.py`

Open the `settings.py` file inside the `geoweb` folder and make the following changes:

### 6.1. Add imports at the top of the file (or near other imports)

```python
import os
from dotenv import load_dotenv
load_dotenv(os.path.join(BASE_DIR, ".env"))
from ctypes.util import find_library
```

### 6.2. Replace the `INSTALLED_APPS` variable with:

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
]
```

### 6.3. Replace the `DATABASES` variable with:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.spatialite",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```

### 6.4. Replace the `TEMPLATES` variable with:

```python
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
```

### 6.5. Add the following variables at the end of `settings.py`:

```python
GDAL_LIBRARY_PATH = find_library("gdal")
GEOS_LIBRARY_PATH = find_library("geos_c")
SPATIALITE_LIBRARY_PATH = "mod_spatialite"
```

## 7. Run migrations and start the development server

In the Codespace terminal, run:

```bash
python manage.py migrate
python manage.py runserver
```

