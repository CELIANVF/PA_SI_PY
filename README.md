# README

## Installation et Configuration du Projet

Ce guide vous aidera à configurer et exécuter le projet. Assurez-vous d'avoir Python installé sur votre machine.

### 1. Création de l'environnement virtuel

Commencez par créer un environnement virtuel pour isoler les dépendances du projet.

```bash
python -m venv ./.venv
```

### 2. Activation de l'environnement virtuel

Activez l'environnement virtuel que vous venez de créer.

#### Sur macOS et Linux
```bash
source ./.venv/bin/activate
```

#### Sur Windows
```bash
.\.venv\Scripts\activate
```

### 3. Aller dans le répertoire du projet

Accédez au répertoire du projet nommé `PA_SI`.

```bash
cd PA_SI
```

### 4. Appliquer les migrations

Exécutez les commandes suivantes pour créer les migrations et appliquer les modifications à la base de données.

```bash
python ./manage.py makemigrations
python ./manage.py migrate
```

### 5. Démarrer le serveur de développement

Lancez le serveur de développement pour pouvoir utiliser l'application.

```bash
python ./manage.py runserver
```

## Utilisation de l'application

### Création de produit

Pour créer un produit, envoyez une requête HTTP POST à l'URL suivante avec les arguments nécessaires dans le corps de la requête :

```
http://localhost:8000/products/create
```

### Exportation des données

Pour exporter les données, accédez à l'URL suivante :

```
http://localhost:8000/products/get
```

## Remarques

- Assurez-vous que votre environnement virtuel est activé chaque fois que vous travaillez sur le projet.
- Si vous rencontrez des problèmes lors de l'exécution de ces commandes, vérifiez que vous êtes bien dans le répertoire du projet `PA_SI` et que l'environnement virtuel est activé.
- Pour arrêter le serveur de développement, utilisez `Ctrl + C` dans le terminal où le serveur est en cours d'exécution
