# Application de Liste de Films à Regarder

Une application en ligne de commande pour gérer votre liste de films à regarder, développée avec Python et SQLite.

## Fonctionnalités

- **Gestion des films** : Ajoutez des films avec leurs dates de sortie
- **Suivi des films à venir** : Visualisez les films dont la sortie est prévue dans le futur
- **Gestion des utilisateurs** : Créez plusieurs utilisateurs pour suivre individuellement les films regardés
- **Suivi des films visionnés** : Marquez les films comme visionnés et consultez votre historique
- **Recherche** : Recherchez des films par titre
- **Stockage persistant** : Toutes les données sont stockées dans une base de données SQLite

## Prérequis

- Python 3.8 ou supérieur
- SQLite3 (inclus avec Python)

## Installation

1. Clonez ce dépôt :
```bash
git clone <url-du-dépôt>
cd A-movie-Watch-List-app-using-python-and-sql
```

2. Aucune dépendance externe n'est requise. L'application utilise uniquement la bibliothèque standard de Python.

## Utilisation

Exécutez l'application depuis la ligne de commande :

```bash
python app.py
```

### Menu Principal

L'application propose les options suivantes :

1. **Ajouter un nouveau film** : Saisissez le titre et la date de sortie (format : jj-mm-AAAA)
2. **Voir les films à venir** : Affiche tous les films dont la date de sortie est dans le futur
3. **Voir tous les films** : Affiche tous les films de la base de données
4. **Marquer un film comme visionné** : Enregistre qu'un utilisateur a regardé un film spécifique
5. **Voir les films visionnés** : Affiche tous les films qu'un utilisateur a regardés
6. **Ajouter un utilisateur** : Crée un nouveau profil utilisateur
7. **Rechercher un film** : Recherche des films par titre partiel
8. **Quitter** : Ferme l'application

## Structure de la Base de Données

L'application utilise trois tables principales :

- **movies** : Stocke les informations des films (id, titre, timestamp de sortie)
- **users** : Stocke les noms d'utilisateur
- **watched** : Table de liaison qui associe les utilisateurs aux films qu'ils ont regardés

## Structure des Fichiers

- `app.py` : Fichier principal de l'application avec l'interface utilisateur
- `database.py` : Fonctions de gestion de la base de données et requêtes SQL
- `data.db` : Fichier de base de données SQLite (créé lors de la première exécution)

## Exemple d'Utilisation

```
Bienvenue dans l'application de liste de films !

1. Ajoutez un nouvel utilisateur (option 6)
2. Ajoutez des films à votre liste (option 1)
3. Marquez les films comme visionnés (option 4)
4. Visualisez vos films visionnés (option 5)
5. Recherchez des films spécifiques (option 7)
```

## Licence

Ce projet est open source et disponible sous licence MIT.
