# Application de Liste de Films à Regarder

Une application de liste de films à regarder développée en Python avec SQLite pour la gestion de base de données.

## Description

Cette application permet aux utilisateurs de gérer leur liste de films à regarder. Les utilisateurs peuvent ajouter des films, suivre les films à venir, marquer les films comme regardés et rechercher des films dans leur collection.

## Fonctionnalités

- **Ajouter un nouveau film** : Ajoutez des films avec leur titre et date de sortie
- **Voir les films à venir** : Consultez les films dont la date de sortie est dans le futur
- **Voir tous les films** : Affichez l'intégralité de votre collection de films
- **Marquer un film comme regardé** : Enregistrez les films que vous avez regardés
- **Voir les films regardés** : Consultez l'historique des films regardés par utilisateur
- **Ajouter un utilisateur** : Créez de nouveaux comptes utilisateurs
- **Rechercher un film** : Trouvez des films par titre (recherche partielle)

## Structure du Projet

- `app.py` : Fichier principal de l'application avec l'interface en ligne de commande
- `database.py` : Module de gestion de la base de données avec toutes les opérations SQL
- `data.db` : Base de données SQLite (créée automatiquement au premier lancement)

## Prérequis

- Python 3.x
- SQLite3 (inclus avec Python)

## Installation

1. Clonez ce dépôt :
```bash
git clone https://github.com/krishna2700/A-movie-Watch-List-app-using-python-and-sql.git
cd A-movie-Watch-List-app-using-python-and-sql
```

2. Aucune dépendance externe n'est requise - l'application utilise uniquement des bibliothèques Python standard.

## Utilisation

Lancez l'application avec la commande suivante :

```bash
python app.py
```

### Menu Principal

L'application affiche un menu interactif avec les options suivantes :

```
1) Ajouter un nouveau film
2) Voir les films à venir
3) Voir tous les films
4) Marquer un film comme regardé
5) Voir les films regardés
6) Ajouter un utilisateur à l'application
7) Rechercher un film
8) Quitter
```

### Exemples d'Utilisation

**Ajouter un film :**
- Sélectionnez l'option 1
- Entrez le titre du film
- Entrez la date de sortie au format jj-mm-AAAA (ou appuyez sur Entrée pour la date du jour)

**Marquer un film comme regardé :**
- Sélectionnez l'option 4
- Entrez votre nom d'utilisateur
- Entrez l'ID du film (visible dans la liste des films)

**Rechercher un film :**
- Sélectionnez l'option 7
- Entrez une partie du titre du film

## Structure de la Base de Données

L'application utilise trois tables principales :

### Table `movies`
- `id` : Identifiant unique (clé primaire)
- `title` : Titre du film
- `release_timestamp` : Date de sortie (timestamp Unix)

### Table `users`
- `username` : Nom d'utilisateur (clé primaire)

### Table `watched`
- `user_username` : Référence à l'utilisateur
- `movie_id` : Référence au film
- Clés étrangères vers les tables `users` et `movies`

## Fonctionnalités Techniques

- Utilisation de SQLite pour le stockage persistant des données
- Gestion des dates avec le module `datetime`
- Index sur la colonne `release_timestamp` pour des performances optimales
- Requêtes SQL paramétrées pour la sécurité
- Interface en ligne de commande interactive

## Auteur

Krishna

## Licence

Ce projet est open source et disponible sous licence libre.
