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

## 6. Check the results and start the development server
In the Codespace terminal, content similar to the image should be printed for command 'python manage.py migrates'.
![Django Successful Migrations](https://github.com/pcelicourt/aguassets/raw/main/images/initialmigration.png)

Run the following to start the development server:
```bash
python manage.py runserver
```
If successful, your interface shoud look like:
![Django WebGIS Successful Launch](https://github.com/pcelicourt/aguassets/raw/main/images/dataloadedinterface.png)
