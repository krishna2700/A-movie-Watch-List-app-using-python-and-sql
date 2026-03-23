# Application de Liste de Films à Regarder

Une application web de liste de films à regarder construite avec Python Flask et SQL.

## Description

Cette application permet aux utilisateurs de gérer une liste personnalisée de films qu'ils souhaitent regarder. Elle offre une interface web intuitive pour ajouter, suivre et organiser vos films préférés avec leurs dates de sortie.

## Fonctionnalités

- ✨ Ajouter des films à votre liste de surveillance
- 📅 Suivre les dates de sortie des films
- 👀 Marquer les films comme visionnés
- 🔍 Rechercher des films dans votre liste
- 👤 Gestion des utilisateurs multiples
- 📊 Voir les films à venir et les films visionnés
- 🗑️ Supprimer des films de votre liste

## Technologies Utilisées

- **Backend**: Python Flask
- **Base de données**: SQLite
- **Frontend**: HTML, CSS, JavaScript
- **API**: RESTful API avec CORS

## Prérequis

- Python 3.x
- Flask
- Flask-CORS

## Installation

1. Clonez le dépôt :
```bash
git clone <url-du-dépôt>
cd A-movie-Watch-List-app-using-python-and-sql
```

2. Installez les dépendances :
```bash
pip install flask flask-cors
```

3. Lancez l'application :
```bash
python app.py
```

4. Ouvrez votre navigateur et accédez à :
```
http://localhost:5000
```

## Structure du Projet

- `app.py` - Application Flask principale avec les routes API
- `database.py` - Gestion de la base de données et opérations CRUD
- `index.html` - Interface utilisateur frontend
- `data.db` - Base de données SQLite

## Points de Terminaison API

### Films

- `GET /api/movies` - Récupérer tous les films
  - Paramètre de requête : `upcoming=true` pour filtrer les films à venir
- `POST /api/movies` - Ajouter un nouveau film
  - Corps : `{ "title": "Titre du film", "release_date": "YYYY-MM-DD" }`
- `DELETE /api/movies/<id>` - Supprimer un film

### Utilisateurs

- `GET /api/users/<username>/watched` - Obtenir les films visionnés par un utilisateur

## Utilisation

1. **Ajouter un film** : Entrez le titre du film et la date de sortie, puis cliquez sur le bouton d'ajout
2. **Marquer comme visionné** : Cliquez sur un film pour le marquer comme visionné
3. **Supprimer un film** : Utilisez le bouton de suppression pour retirer un film de votre liste
4. **Voir les statistiques** : Consultez le nombre total de films et les films à venir dans le tableau de bord

## Fonctionnalités de la Base de Données

L'application crée automatiquement les tables nécessaires au démarrage :
- Table des films (titre, horodatage de sortie)
- Table des utilisateurs
- Table de suivi des films visionnés

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à soumettre des pull requests ou à ouvrir des issues.

## Licence

Ce projet est open source et disponible sous licence MIT.

## Auteur

Créé avec ❤️ pour les cinéphiles du monde entier
