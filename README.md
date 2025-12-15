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

## 4.4 Check and run migrations in addition to the Django server

In the Codespace terminal, you can check the content of the migrations files with the geoweb/geowebapp/migrations/ folder. Then, run the following command in the terminal.

```bash
python manage.py migrate
python manage.py runserver
```

### 4.5 Replace the `INSTALLED_APPS` variable with:
Here I have pre-created a new app named 'geowebapis' using the command 'python manage.py startapp geowebapis'.
I have populated it with some contents necessary for the next steps of the activity.

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
## 6. Launch the Django server and check the Codespace terminal
```bash
python manage.py runserver
```
You can select one sensor name or code in the Django app interface and check the terminal:
![Launch CodeSpace](https://github.com/pcelicourt/aguassets/raw/main/images/urlnotfound.png)

## 7. Files editing to solve the URLs that are not found
### 7.1 Template File
we will click on and look at Line 97 of the template file: /geowebapp/templates/index.html
We see the instruction: <script src="{% static 'js/eventhandler.js' %}"></script> 
It indicates that there template must include a file named eventhandler.js located inside the /geoweb/static/ folder.

### 7.2 Static File
We will click on and inspect that file /geoweb/static/eventhandler.js at three different points:

Line 19: We see the following code that defines a function getSensorByName() to be called when user selects a sensor in the interface acoording to Line 53 of the template /geowebapp/static/index.html:
<select class="form-select" id="dropdwn" data-live-search="true" onchange="getSensorByName()">

```JS
function getSensorByName() {
    var dropdown = document.getElementById('dropdwn');
    if (!dropdown) return;
    var sensorCode = dropdown.value;
    console.log("Selected sensor from dropdown:", sensorCode);
    fetch("sensor/", {
        method: "POST",
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': csrftoken,
        },
        body: `sensor_name=${sensorCode}`
    }) .....
```
In this function, we need to spot the entry point or url to the server. It is: "sensor/" that the function fetch will request and which must be defined in the backend. 
The same applies for Line 39 and Line 96, but for Line 96, we have a different url "user-location/" which must be defined in the back-end as well. 

### 7.3 URL files
We will start with the 




