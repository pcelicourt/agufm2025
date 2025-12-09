# Tutorial \#2 for the American Geophysical Union Fall Meeting 2025
This tutorial will help you prepare the DB for the next step, which is the loading of the spatial and timeseries data into the DB

## 1. Connect to your existing account

- [GitHub Sign in](https://github.com/login?)

## 2. Access the workshop GitHub repository

Click the following link to open the workshop repository: [AGUFM 2025 Workshop GitHub Repo](https://github.com/pcelicourt/agufm2025/tree/geodjangoapp).

## 3. Create a codespace from the branch geodjangoapp

With the branch geodjangoapp selected in the agufm202 repo, click the + sign to create a codespace from the branch as demonstrated in the image below:

![Launch CodeSpace](https://github.com/pcelicourt/aguassets/raw/main/images/geodjangosetupinit.png)

## 4. Codespace development environment

Your Codespace development environment should look similar to this:

![CodeSpace Terminal](https://github.com/pcelicourt/aguassets/raw/main/images/geodjangosetupinterface.png)

## 5. Continue the Django WebGIS Application development
In the Codespace terminal, run the following commands.

### 5.1. Verify Python and Django versions in the Codespace terminal

```bash
source .venv/bin/activate
python --version
pip install -r requirements.txt
python -m django --version
```

### 5.3. Change into the `geoweb` directory
Note that you must execute the following commands containing 'python -m manage ...' or 'python manage.py ...' within the geoweb folder.

```bash
cd geoweb
```

## 5.4 Check the Model, run migrations and start the development server

In the Codespace terminal, you can check the content of the Model component (models.py) with the geowebapp folder. Then, run the following commands in the terminal.
The first command will convert the ODM2 classes defined in models.py into a migration file that the second command will load into the DB.

```bash
python manage.py makemigrations
python manage.py migrate
```
## 6. Check the results
In the Codespace terminal, content similar to the image should be printed.
![Django Successful Migrations](https://github.com/pcelicourt/aguassets/raw/main/images/odm2migration.png)
