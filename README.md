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

![Terminal du Codespace](https://github.com/pcelicourt/aguassets/raw/main/images/odm2loadercodespace.png)

## 5. Poursuivre le développement de l’application

Dans le terminal du Codespace, exécutez les commandes suivantes.

### 5.1. Activer l'environnement virtuel et installer les bibliothèques

Dans le terminal du Codespace, exécutez les commandes suivantes :

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

### 5.2. Accéder au répertoire racine `geoweb`

Vous devez exécuter les commandes contenant `python -m manage ...` ou `python manage.py ...` à l’intérieur du dossier `geoweb`.

```bash
cd geoweb
```

### 5.3. Vérifier et exécuter les migrations

Dans le terminal du Codespace, vous pouvez vérifier le contenu des fichiers de migration dans le dossier suivant :

```text
geoweb/geowebapp/migrations/
```

Ensuite, exécutez la commande suivante dans le terminal :

```bash
python manage.py migrate
```

## 6. Vérifier les résultats et démarrer le serveur de développement

Dans le terminal du Codespace, un contenu similaire à celui de l’image devrait s’afficher après l’exécution de la commande suivante :

```bash
python manage.py migrate
```

![Migrations Django réussies](https://github.com/pcelicourt/aguassets/raw/main/images/initialmigration.png)

Exécutez la commande suivante pour démarrer le serveur de développement :

```bash
python manage.py runserver
```

Si le lancement est réussi, votre interface devrait ressembler à ceci :

![Lancement réussi de Django WebGIS](https://github.com/pcelicourt/aguassets/raw/main/images/dataloadedinterface.png)
