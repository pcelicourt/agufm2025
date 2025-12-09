# Tutorial for the American Geophysical Union Fall Meeting 2025

# Following the setup of the agufm25 template in CodeSpaces, run the following commands to create a Django WebGIS Application in your terminal

# CodeSpaces Terminal
$ source .venv/bin/activate

$ python --version

$ python -m django --version


## Change to the newly created directory geoweb
$ cd geoweb



# In the settings.py file within the geoweb folder


# Check the models.py module


# CodeSpaces Terminal: Run the following command to launch the Django application
$ cd geoweb
$ python manage.py migrate
$ python manage.py runserver


# The Model
## With the module models.py populated, run the following commands to populate the DB
$ python manage.py makemigrations
$ python manage.py migrate
