# Application de Liste de Films à Regarder

Une application de gestion de liste de films à regarder développée en Python et SQLite.

## Description

Cette application permet aux utilisateurs de gérer leur liste de films à regarder. Les utilisateurs peuvent ajouter des films, suivre les films à venir, marquer les films comme regardés et rechercher des films dans leur collection.

## Fonctionnalités

- **Ajouter des films** : Ajoutez de nouveaux films avec leur titre et date de sortie
- **Voir les films à venir** : Consultez les films dont la sortie est prévue dans le futur
- **Voir tous les films** : Affichez l'intégralité de votre collection de films
- **Marquer comme regardé** : Enregistrez les films que vous avez regardés
- **Historique de visionnage** : Consultez les films regardés par utilisateur
- **Gestion des utilisateurs** : Ajoutez des utilisateurs à l'application
- **Recherche** : Recherchez des films par titre (recherche partielle)

## Structure du Projet

- `app.py` : Application principale avec interface en ligne de commande
- `database.py` : Gestion de la base de données SQLite et requêtes
- `data.db` : Base de données SQLite contenant les films, utilisateurs et historique de visionnage

## Schéma de Base de Données

### Table `movies`
- `id` : Identifiant unique (clé primaire)
- `title` : Titre du film
- `release_timestamp` : Date de sortie (timestamp)

### Table `users`
- `username` : Nom d'utilisateur (clé primaire)

### Table `watched`
- `user_username` : Nom d'utilisateur (clé étrangère)
- `movie_id` : Identifiant du film (clé étrangère)

## Installation

1. Clonez ce dépôt
2. Assurez-vous d'avoir Python 3.8 ou supérieur installé
3. Aucune dépendance externe n'est requise (utilise uniquement les bibliothèques standard de Python)

## Utilisation

Lancez l'application avec la commande suivante :

```bash
python app.py
```

### Menu Principal

L'application affiche un menu interactif avec les options suivantes :

1. Ajouter un nouveau film
2. Voir les films à venir
3. Voir tous les films
4. Marquer un film comme regardé
5. Voir les films regardés
6. Ajouter un utilisateur à l'application
7. Rechercher un film
8. Quitter

## Format de Date

Les dates doivent être saisies au format : `jj-mm-AAAA` (par exemple : 25-12-2024)

Si aucune date n'est fournie lors de l'ajout d'un film, la date actuelle sera utilisée par défaut.

## Exemples d'Utilisation

### Ajouter un Film
```
Movie title: Inception
Release date (dd-mm-YYYY): 16-07-2010
```

### Marquer un Film comme Regardé
```
Username: john
Movie ID: 1
```

### Rechercher un Film
```
Enter partial movie title: incep
```

## Technologies Utilisées

- **Python 3** : Langage de programmation principal
- **SQLite3** : Base de données relationnelle légère
- **datetime** : Gestion des dates et timestamps

## Licence

Ce projet est un exemple éducatif d'application de gestion de films.
