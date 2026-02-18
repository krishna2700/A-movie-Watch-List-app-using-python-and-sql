# Application de Liste de Films à Regarder

Une application en ligne de commande pour gérer une liste de films à regarder, construite avec Python et SQLite.

## Description

Cette application permet d'ajouter des films, de consulter les sorties à venir, de suivre les films visionnés par utilisateur et de rechercher des titres dans la base de données.

## Fonctionnalités

- ✅ Ajouter de nouveaux films avec leur date de sortie
- 📅 Afficher les films à venir
- 📋 Consulter tous les films enregistrés
- ✓ Marquer des films comme visionnés
- 🎬 Voir l'historique des films visionnés par utilisateur
- 👤 Gérer plusieurs utilisateurs
- 🔍 Rechercher des films par titre

## Structure du Projet

```
.
├── app.py          # Application principale (CLI)
├── database.py     # Gestion de la base de données SQLite
├── data.db         # Base de données SQLite (générée automatiquement)
└── README.md       # Documentation
```

## Prérequis

- Python 3.8 ou supérieur
- SQLite3 (inclus avec Python)

## Installation

1. Clonez le dépôt :
```bash
git clone <url-du-depot>
cd <nom-du-repertoire>
```

2. Aucune dépendance externe n'est nécessaire.

## Utilisation

Lancez l'application avec :

```bash
python app.py
```

### Menu principal

```
Please select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Add watched movie
5) View watched movies.
6) Add user to the app.
7) Search for a movie.
8) Exit.
```

### Guide rapide

- **Ajouter un film** : option `1`, titre puis date `jj-mm-AAAA`.
- **Voir les films à venir** : option `2`.
- **Voir tous les films** : option `3`.
- **Marquer comme visionné** : option `4`, nom d'utilisateur puis ID du film.
- **Voir les films visionnés** : option `5`.
- **Ajouter un utilisateur** : option `6`.
- **Rechercher un film** : option `7`.

## Base de Données

L'application utilise trois tables principales :

- **movies** : `id`, `title`, `release_timestamp`
- **users** : `username`
- **watched** : `user_username`, `movie_id`

Un index est créé sur `release_timestamp` pour les films à venir.

## Exemple d'utilisation

```
Welcome to the watchlist app!
Please select one of the following options:
1) Add new movie.
...

Your selection: 6
Username: alice

Your selection: 1
Movie title: Inception
Release date (dd-mm-YYYY): 16-07-2010

Your selection: 4
Username: alice
Movie ID: 1

Your selection: 5
Username: alice
-- Watched movies --
1: Inception (on Jul 16 2010)
----
```

## Améliorations possibles

- Interface graphique (GUI)
- Notes et évaluations de films
- Catégories et genres
- Import/export de données
- Intégration avec une API de films

## Licence

Projet d'exemple à visée éducative.
