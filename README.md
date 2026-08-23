# Tutoriel n° 1 : École d'été 2026 du RQRAD

Ce tutoriel vous aidera à charger des données spatiales et des séries temporelles dans la base de données fondée sur ODM2.


- [Se connecter avec GitHub](https://github.com/login?)
## 1. Créer un compte GitHub OU se connecter à votre compte existant

- [GitHub Signup](https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home)  
- [GitHub Sign in](https://github.com/login?)

## 2. Accéder au dépôt GitHub de l’atelier

Cliquez sur le lien suivant pour ouvrir le dépôt de l’atelier :

[**Dépôt GitHub de l’atelier **](https://github.com/pcelicourt/agufm2025/tree/rqrad2026)

## 3. Créer un Codespace à partir de la branche `rqrad2026`

Une fois la branche `rqrad2026` sélectionnée dans le dépôt `agufm2025`, cliquez sur le signe `+` pour créer un Codespace à partir de cette branche, comme illustré dans l’image ci-dessous :

![Lancer le Codespace](https://github.com/pcelicourt/aguassets/blob/main/images/rqrad.png)

## 4. Environnement de développement du Codespace

Votre environnement de développement Codespace devrait ressembler à ceci :

![Terminal du Codespace](https://github.com/pcelicourt/aguassets/raw/main/images/codespacerqrad.png)

## 5. Poursuivre le développement de la base de données

Dans le terminal du Codespace, exécutez les commandes suivantes.

### 5.1. Créer et Activer  un environnement virtuel et installer les bibliothèques
Note: Un environnement virtuel Python est un dossier isolé qui contient une copie de l'interpréteur Python et ses propres bibliothèques. Il évite les conflits de versions entre les différents projets de votre ordinateur. Voir ![Environnement Virtuel](https://docs.python.org/fr/3/tutorial/venv.html)

Dans le terminal du Codespace, exécutez les commandes suivantes :

```bash
python -m venv .rqrad
source .rqrad/bin/activate
pip install -r requirements.txt
```

### 5.2. Accéder au répertoire racine `geoweb`

```bash
cd geoweb
```

## 5.3. Vérifier le modèle, exécuter les migrations
On va vérifier ensemble la construction de chaque table surtout la SamplingFeatures.
Dans l'interface de Codespace, vous pouvez vérifier le contenu du le fichier (`models.py`) contenant les tables de l'ODM2 localisé ici: `geoweb/geowebapp/models.py`. 
En particulier, vérifier la construction de la table SamplingFeatures.
Ensuite, exécutez les commandes suivantes dans le terminal.

La première commande convertira les classes ODM2 définies dans `models.py` en un fichier de migration que la seconde commande chargera dans la base de données qui sera créée automatiquement et localisé ici: `geoweb/db.sqlite3`.

```bash
#Cette commande crée un nouveau fichier `0001_initial.py` dans le dossier `geoweb/geowebapp/migrations`
python manage.py makemigrations
python manage.py migrate
```

## 5.4. Vérifier les résultats

Dans le terminal de Codespace, un contenu similaire à l'image devrait s'afficher pour la commande `python manage.py makemigrations` :

![Migrations ODM2 réussies](https://github.com/pcelicourt/aguassets/raw/main/images/codespacerqradmigrinit.png)

Dans le terminal de Codespace, un contenu similaire à l'image devrait s'afficher pour la commande `python manage.py migrate` :

![Migrations initiales réussies](https://github.com/pcelicourt/aguassets/raw/main/images/codespacerqradmigrinitm.png)

## 5.5. Vérifier le contenu de la base de données ? 

À cause de la dimension spatiale du modèle de données, la visualisation des tables créées est possible seulement avec un outil spécial comme QGIS, SpatialiteGUI, et DBeaver.  

## 6. Insertion d'informations dans les tables
L'écosystème Django ne permet pas la création de migrations automatiques pour autres transactions que les modèles. Donc, nous devons créer nos propres migrations. Pour ce faire, on va créer des migrations vides que nous allons remplir par la suite.

### 6.1. Insertion des vocabulaires contrôlés
Les vocabulaires contrôlés de l'ODM2 ont été téléchargées sous le format csv et stockés dans le dossier  `geoweb/geowebapp/static/data/odm2cv`.

Exécutez la commande suivante dans le terminal de CodeSpace  
```bash
#Cette commande crée un nouveau fichier `000X_auto_YYYYMMDD_HHMM.py` (ex: 0002_auto_20250611_1156.py) dans le dossier `geoweb/geowebapp/migrations`
python manage.py makemigrations --empty geowebapp
```
Localiser le fichier créé, remplacer tout son contenu par les codes Python suivants (copier de la ligne 93 à 146) 
puis sauvegarder le fichier. Assurez-vous de remplacer le pas d'accès et le nom de table manquants dans le dictionnaire cv_files_path

```bash
from django.db import migrations

import csv
from pathlib import Path

# Define the mapping of model names from models.py to their corresponding CSV file paths
cv_files_path = {"CV_SamplingFeatureType": "static/data/odm2cv/samplingfeaturetype.csv",
                  "CV_SamplingFeatureGeoType": "static/data/odm2cv/samplingfeaturegeotype.csv",
                  "CV_ElevationDatum": "static/data/odm2cv/elevationdatum.csv",
                  "CV_VariableType": "static/data/odm2cv/variabletype.csv",
                  "CV_UnitsType": " ", #Ajouter le pas d'accès du fichier correspondant
                  " ": "static/data/odm2cv/variablename.csv", # Ajouter le nom de la table correspondant
                  "CV_RelationshipType": "static/data/odm2cv/relationshiptype.csv",
                  "CV_Medium": "static/data/odm2cv/medium.csv",
                  "CV_OrganizationType": "static/data/odm2cv/organizationtype.csv",
                  "CV_Speciation": "static/data/odm2cv/speciation.csv",
                  "CV_Status": "static/data/odm2cv/status.csv",
                  "CV_TaxonomicClassifierType": "static/data/odm2cv/taxonomicclassifiertype.csv",
                  "CV_ActionType": "static/data/odm2cv/actiontype.csv",
                  "CV_AggregationStatistic": "static/data/odm2cv/aggregationstatistic.csv",
                  "CV_QualityCode": "static/data/odm2cv/qualitycode.csv",
                  "CV_CensorCode": "static/data/odm2cv/censorcode.csv",
                  "CV_ResultType": "static/data/odm2cv/resulttype.csv",
                  "CV_MethodType": "static/data/odm2cv/methodtype.csv",
                  "CV_SiteType": "static/data/odm2cv/sitetype.csv",
                  "CV_DataQualityType": "static/data/odm2cv/dataqualitytype.csv",
                }

# Function to load CSV data into the corresponding models
def load_cvs(apps, schema_editor):
    for model_name, file_path in cv_files_path.items():
        model = apps.get_model('geowebapp', model_name) # model = apps.get_model('geowebapp', "CV_SamplingFeatureType")
        full_file_path = Path(__file__).resolve().parent.parent / file_path # Get the full path to the CSV file relative to the current migration file

        with open(full_file_path, newline='\n', encoding="utf8") as csvfile:
            cvs = csv.reader(csvfile, delimiter=',')
            next(cvs) # Skip the header row of the CSV file
            for cv in cvs:
                term, name, definition, category, sourcevocabularyuri, _, _ = cv # Unpack the values from the CSV row
                model(term=term, name=name,
                      definition=definition, category=category,
                      sourcevocabularyuri=sourcevocabularyuri
                    ).save() # Create and save a new instance of the model with the values from the CSV row

# Define the migration class
class Migration(migrations.Migration):

    dependencies = [
        ("geowebapp", "0001_initial"), # Specify the dependency on the initial migration of the geowebapp app
    ]

    operations = [
        migrations.RunPython(load_cvs) # Run the load_cvs function to populate the models with data from the CSV files
    ]
```

Exécuter la commande suivante dans le terminal de CodeSpace pour insérer les vocabulaires contrôlés dans les tables correspondantes
```bash
#Cette commande crée un nouveau fichier `0001_initial.py` dans le dossier `geoweb/geowebapp/migrations`
python manage.py migrate
```

### 6.2. Insertion de l'information sur les entités gestionnaires des données
On va répéter les trois étapes précédentes : les mêmes commandes mais des codes différents (ci-dessous).
Vous pouvez personnaliser les codes de la Ligne 160 à 215 avec vos propres informations.
```bash
from datetime import date

from django.db import migrations

# Define the function to load contact data into the database (we will work with the Organizations (1), People (2), and Affiliations (3) models)
def load_contact_data(apps, schema_editor):
    Organizations = apps.get_model('geowebapp', 'Organizations') # Get the Organizations model from the geowebapp app
    CV_OrganizationType = apps.get_model('geowebapp', 'CV_OrganizationType') # Get the CV_OrganizationType model from the geowebapp app

    People = apps.get_model('geowebapp', 'People') # Get the People model from the geowebapp app

    Affiliations = apps.get_model('geowebapp', 'Affiliations') # Get the Affiliations model from the geowebapp app

    organization_type = CV_OrganizationType.objects.filter(term='university').first() # Get the first instance of CV_OrganizationType with the term 'university'

    # Create and save a new instance of the Organizations model with the specified attributes
    # You could add your own organization details here, or modify the existing ones as needed
    organization = Organizations(
        organizationcode='WSU', # modifier ici si vous le souhaitez
        organizationname='Washington State University', # modifier ici si vous le souhaitez
        organizationdescription='A public land-grant research university in Pullman, Washington, United States', # modifier ici si vous le souhaitez
        organizationlink='https://css.wsu.edu/', # modifier ici si vous le souhaitez
        organizationtypecv=organization_type, 
    )
    organization.save()

    # Create and save a new instance of the People model with the specified attributes
    contact_person = People(
        personfirstname='David', # modifier ici si vous le souhaitez
        personlastname='Brown' # modifier ici si vous le souhaitez
    )
    contact_person.save()

    # Create and save a new instance of the Affiliations model with the specified attributes
    affiliation = Affiliations(
        personid=contact_person,
        organizationid=organization,
        isprimaryorganizationcontact=True,
        affiliationstartdate=date(2002, 1, 1), # modifier ici si vous le souhaitez
        primaryphone='509-332-2756', # modifier ici si vous le souhaitez
        primaryemail='dave.brown@wsu.edu', # modifier ici si vous le souhaitez
        primaryaddress='Pullman, WA, USA', # modifier ici si vous le souhaitez
        personlink='https://bsyse.wsu.edu/people/faculty/wsu-profile/dave.brown/' # modifier ici si vous le souhaitez
    )
    affiliation.save()


class Migration(migrations.Migration):

    dependencies = [
        ("geowebapp", "0002_auto_YYYYMMDD_HHMM"), # Ajouter ici le nom de votre deuxième fichier de migrations
    ]

    operations = [
        migrations.RunPython(load_contact_data)
    ]

```

### 6.2. Insertion du polygone délimitant la ferme
À partir d'ici, on va télécharger les fichiers de migration ci-dessous et les téléverser dans le dossier migrations localisé ici:
`geoweb/geowebapp/migrations`
![Fichier de migration de données de délimitation de la ferme](https://github.com/pcelicourt/aguassets/blob/main/migrationsdemo/0004_auto_20250612_1522.py)

### 6.3. Insertion des polygones délimitant les champs
![Fichier de migration de données de délimitation de la ferme](https://github.com/pcelicourt/aguassets/blob/main/migrationsdemo/0005_auto_20250612_1522.py)

### 6.4. Insertion des polygones délimitant les parcelles
![Fichier de migration de données de délimitation des parcelles](https://github.com/pcelicourt/aguassets/blob/main/migrationsdemo/0006_auto_20250612_1522.py)

### 6.5. Insertion de la géolocalisation des capteurs de mesure de température et d'humidité du sol
![Fichier de migration de données de géopositionnement des capteurs](https://github.com/pcelicourt/aguassets/blob/main/migrationsdemo/0007_auto_20250612_1530.py)

### 6.6. Insertion des données des capteurs 
![Fichier de migration des séries temporelles](https://github.com/pcelicourt/aguassets/blob/main/migrationsdemo/0008_auto_20250612_2244.py)

## 7. Visualisation rapide des résultats 
Exécutez la commande suivante pour démarrer le serveur de développement :

```bash
python manage.py runserver
```
Si le lancement est réussi, votre interface devrait ressembler à ceci :

![Lancement réussi de l'interface de visualisation des données stockées](https://github.com/pcelicourt/aguassets/raw/main/images/dataloadedinterface.png)
