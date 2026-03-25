# Application de Liste de Films à Regarder

Une application de liste de films développée en Python avec une base de données SQL pour gérer vos films à regarder et suivre ceux que vous avez déjà vus.

## Description

Cette application de ligne de commande permet aux utilisateurs de gérer une liste personnalisée de films. Vous pouvez ajouter de nouveaux films, suivre vos films regardés, rechercher des films et bien plus encore.

## Fonctionnalités

- **Ajouter un nouveau film** : Ajoutez des films avec leur titre et date de sortie
- **Voir les films à venir** : Consultez les films qui sortiront prochainement
- **Voir tous les films** : Affichez l'intégralité de votre liste de films
- **Marquer un film comme vu** : Enregistrez les films que vous avez regardés
- **Voir les films regardés** : Consultez votre historique de visionnage
- **Gestion des utilisateurs** : Ajoutez des utilisateurs à l'application
- **Recherche de films** : Recherchez des films par titre partiel
- **Stockage persistant** : Toutes les données sont stockées dans une base de données SQLite

## Prérequis

- Python 3.8 ou supérieur
- SQLite (inclus avec Python)

## Installation

1. Clonez ce dépôt :
```bash
git clone <url-du-dépôt>
cd A-movie-Watch-List-app-using-python-and-sql
```

2. Assurez-vous que Python est installé sur votre système :
```bash
python --version
```

## Utilisation

Lancez l'application en exécutant :

```bash
python app.py
```

### Menu Principal

Une fois l'application lancée, vous verrez un menu avec les options suivantes :

1. **Ajouter un nouveau film** - Entrez le titre et la date de sortie
2. **Voir les films à venir** - Affiche les films dont la date de sortie est dans le futur
3. **Voir tous les films** - Liste complète de tous les films enregistrés
4. **Ajouter un film regardé** - Marquez un film comme vu pour un utilisateur
5. **Voir les films regardés** - Consultez les films regardés par un utilisateur
6. **Ajouter un utilisateur** - Créez un nouveau compte utilisateur
7. **Rechercher un film** - Recherchez des films par titre
8. **Quitter** - Fermez l'application

### Exemple d'Utilisation

```
Bienvenue dans l'application de liste de films !
Veuillez sélectionner une des options suivantes :
1) Ajouter un nouveau film.
2) Voir les films à venir.
...
Votre sélection : 1

Titre du film : Inception
Date de sortie (jj-mm-AAAA) : 16-07-2010
```

## Structure du Projet

- `app.py` - Point d'entrée principal de l'application avec l'interface utilisateur
- `database.py` - Gestion de la base de données et requêtes SQL
- `data.db` - Fichier de base de données SQLite
- `logo.svg` - Logo de l'application

## Format des Dates

Les dates doivent être saisies au format `jj-mm-AAAA` (jour-mois-année).
Si aucune date n'est fournie lors de l'ajout d'un film, la date actuelle sera utilisée par défaut.

## Base de Données

L'application utilise SQLite pour stocker :
- Les informations sur les films (titre, date de sortie)
- Les utilisateurs
- Les relations entre utilisateurs et films regardés

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou soumettre une pull request.

## Licence

Ce projet est un projet éducatif open source.
