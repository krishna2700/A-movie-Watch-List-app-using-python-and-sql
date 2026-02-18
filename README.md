# Application de Liste de Films à Regarder

Une application de gestion de liste de films à regarder utilisant Python et SQL (SQLite).

## Description

Cette application permet aux utilisateurs de gérer une liste de films qu'ils souhaitent regarder. Elle offre des fonctionnalités complètes pour ajouter des films, suivre ceux qui ont été visionnés, et gérer plusieurs utilisateurs.

## Fonctionnalités

- ✅ **Ajouter de nouveaux films** avec leur date de sortie
- 📅 **Voir les films à venir** (films avec une date de sortie future)
- 📋 **Voir tous les films** de la base de données
- ✓ **Marquer les films comme visionnés** par utilisateur
- 🎬 **Consulter l'historique des films visionnés** par utilisateur
- 👤 **Gérer plusieurs utilisateurs** dans l'application
- 🔍 **Rechercher des films** par titre (recherche partielle)

## Structure du Projet

```
.
├── app.py          # Application principale avec interface en ligne de commande
├── database.py     # Gestion de la base de données SQLite
├── data.db         # Base de données SQLite (générée automatiquement)
└── README.md       # Ce fichier
```

## Prérequis

- Python 3.8 ou supérieur
- Bibliothèque SQLite3 (incluse avec Python)

## Installation

1. Clonez ce dépôt :
```bash
git clone <url-du-depot>
cd <nom-du-repertoire>
```

2. Aucune dépendance externe n'est requise - SQLite3 est inclus avec Python.

## Utilisation

Lancez l'application avec :

```bash
python app.py
```

### Menu Principal

Lors de l'exécution, vous verrez le menu suivant :

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

### Guide d'Utilisation

#### 1. Ajouter un film
- Sélectionnez l'option `1`
- Entrez le titre du film
- Entrez la date de sortie au format `jj-mm-AAAA` (ou appuyez sur Entrée pour la date actuelle)

#### 2. Voir les films à venir
- Sélectionnez l'option `2`
- Affiche tous les films dont la date de sortie est dans le futur

#### 3. Voir tous les films
- Sélectionnez l'option `3`
- Affiche l'ensemble des films de la base de données

#### 4. Marquer un film comme visionné
- Sélectionnez l'option `4`
- Entrez le nom d'utilisateur
- Entrez l'ID du film (visible dans les listes de films)

#### 5. Voir les films visionnés
- Sélectionnez l'option `5`
- Entrez le nom d'utilisateur
- Affiche tous les films que cet utilisateur a marqués comme visionnés

#### 6. Ajouter un utilisateur
- Sélectionnez l'option `6`
- Entrez un nom d'utilisateur unique

#### 7. Rechercher un film
- Sélectionnez l'option `7`
- Entrez un terme de recherche (recherche partielle dans les titres)

#### 8. Quitter
- Sélectionnez l'option `8` pour fermer l'application

## Structure de la Base de Données

L'application utilise SQLite avec trois tables principales :

### Table `movies`
- `id` : Identifiant unique (clé primaire)
- `title` : Titre du film
- `release_timestamp` : Date de sortie (timestamp Unix)

### Table `users`
- `username` : Nom d'utilisateur (clé primaire)

### Table `watched`
- `user_username` : Nom d'utilisateur (clé étrangère)
- `movie_id` : ID du film (clé étrangère)

Un index est créé sur `release_timestamp` pour optimiser les requêtes de films à venir.

## Exemple d'Utilisation

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

## Développement

### Fichiers Principaux

**`app.py`** : Contient la logique de l'interface utilisateur
- Menu interactif en ligne de commande
- Fonctions de saisie et d'affichage
- Formatage des dates

**`database.py`** : Gestion de la base de données
- Création des tables
- Opérations CRUD (Create, Read, Update, Delete)
- Requêtes SQL préparées pour la sécurité

## Améliorations Futures

- [ ] Interface graphique (GUI)
- [ ] Notation des films
- [ ] Catégories et genres
- [ ] Import/export de données
- [ ] Recommandations de films
- [ ] Intégration avec des API de films (TMDb, OMDB)

## Licence

Ce projet est un exemple éducatif de gestion de base de données avec Python.

## Auteur

Projet de démonstration pour l'apprentissage de Python et SQL.
