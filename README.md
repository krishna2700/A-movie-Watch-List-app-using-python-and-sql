# Application de Liste de Films à Regarder

Une application de liste de films interactive développée en Python avec SQLite pour gérer votre collection de films et suivre ce que vous avez regardé.

## 📋 Description

Cette application vous permet de gérer une liste de films personnalisée avec les fonctionnalités suivantes :
- Ajouter de nouveaux films avec leurs dates de sortie
- Visualiser les films à venir
- Suivre les films que vous avez regardés
- Gérer plusieurs utilisateurs
- Rechercher des films par titre

## 🚀 Fonctionnalités

1. **Ajouter un nouveau film** - Enregistrez des films avec leur titre et date de sortie
2. **Voir les films à venir** - Affichez uniquement les films dont la date de sortie est dans le futur
3. **Voir tous les films** - Consultez l'intégralité de votre collection de films
4. **Marquer un film comme regardé** - Enregistrez quand un utilisateur a regardé un film
5. **Voir les films regardés** - Consultez l'historique des films regardés par utilisateur
6. **Ajouter un utilisateur** - Créez de nouveaux profils utilisateurs
7. **Rechercher un film** - Trouvez des films par recherche partielle du titre
8. **Quitter** - Fermez l'application

## 🛠️ Technologies Utilisées

- **Python 3** - Langage de programmation principal
- **SQLite3** - Base de données pour le stockage persistant
- **datetime** - Gestion des dates et timestamps

## 📦 Structure de la Base de Données

L'application utilise trois tables principales :

### Table `movies`
- `id` (INTEGER PRIMARY KEY) - Identifiant unique du film
- `title` (TEXT) - Titre du film
- `release_timestamp` (REAL) - Date de sortie en format timestamp

### Table `users`
- `username` (TEXT PRIMARY KEY) - Nom d'utilisateur unique

### Table `watched`
- `user_username` (TEXT) - Référence à l'utilisateur
- `movie_id` (INTEGER) - Référence au film
- Clés étrangères vers les tables users et movies

## 🎯 Installation et Utilisation

### Prérequis
- Python 3.8 ou supérieur
- SQLite3 (généralement inclus avec Python)

### Lancement de l'Application

```bash
python app.py
```

### Utilisation

1. Au démarrage, l'application affiche un menu avec 8 options
2. Entrez le numéro correspondant à l'action souhaitée
3. Suivez les instructions pour chaque fonctionnalité
4. Les données sont automatiquement sauvegardées dans `data.db`

### Exemple d'Utilisation

```
Bienvenue dans l'application de liste de films !

Veuillez sélectionner une des options suivantes :
1) Ajouter un nouveau film.
2) Voir les films à venir.
3) Voir tous les films
4) Ajouter un film regardé
5) Voir les films regardés.
6) Ajouter un utilisateur à l'application.
7) Rechercher un film.
8) Quitter.

Votre sélection : 1
Titre du film : Inception
Date de sortie (jj-mm-AAAA) : 16-07-2010
```

## 📁 Fichiers du Projet

- `app.py` - Point d'entrée principal de l'application avec l'interface utilisateur
- `database.py` - Gestion de la base de données et requêtes SQL
- `data.db` - Fichier de base de données SQLite (créé automatiquement)
- `README.md` - Ce fichier de documentation

## 🔍 Fonctionnalités Techniques

- **Gestion des dates** : Format d'entrée `jj-mm-AAAA`, stockage en timestamp Unix
- **Index de performance** : Index créé sur `release_timestamp` pour des requêtes rapides
- **Recherche flexible** : Recherche partielle de titre avec l'opérateur SQL `LIKE`
- **Gestion des relations** : Utilisation de clés étrangères pour l'intégrité des données

## 💡 Améliorations Futures Possibles

- Interface graphique (GUI)
- Notation des films
- Catégories et genres
- Import/Export de données
- Recommandations de films
- Intégration avec des API de films (TMDB, OMDB)

## 📝 Notes

- Si aucune date n'est fournie lors de l'ajout d'un film, la date du jour est utilisée par défaut
- Les films à venir sont filtrés en fonction de la date actuelle
- Chaque utilisateur peut suivre ses propres films regardés

## 🤝 Contribution

Ce projet est un exemple éducatif d'application Python avec base de données SQLite.

---

**Développé avec Python et SQLite** 🐍 💾
