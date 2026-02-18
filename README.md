# 🎬 Application de Liste de Films à Regarder

Une application en ligne de commande développée en **Python** et **SQLite** permettant de gérer une liste personnelle de films à regarder.

## 📋 Description

Cette application permet aux utilisateurs de créer et gérer une liste de films. Vous pouvez ajouter des films, suivre ceux que vous avez déjà regardés, rechercher des films par titre et gérer plusieurs utilisateurs.

## 🚀 Fonctionnalités

- **Ajouter un film** — Enregistrer un nouveau film avec son titre et sa date de sortie.
- **Voir les films à venir** — Afficher uniquement les films dont la date de sortie est dans le futur.
- **Voir tous les films** — Lister l'ensemble des films enregistrés dans la base de données.
- **Marquer un film comme vu** — Associer un film regardé à un utilisateur.
- **Voir les films regardés** — Consulter la liste des films vus par un utilisateur donné.
- **Ajouter un utilisateur** — Créer un nouveau profil utilisateur dans l'application.
- **Rechercher un film** — Trouver un film par une recherche partielle sur le titre.

## 🛠️ Technologies Utilisées

| Technologie | Utilisation |
|-------------|-------------|
| Python 3    | Langage principal |
| SQLite      | Base de données locale |

## 📁 Structure du Projet

```
.
├── app.py          # Point d'entrée de l'application (interface utilisateur)
├── database.py     # Couche d'accès aux données (requêtes SQL)
├── data.db         # Base de données SQLite
└── README.md       # Documentation du projet
```

## ⚙️ Prérequis

- **Python 3.6** ou version supérieure
- Aucune dépendance externe requise (utilise uniquement les bibliothèques standard de Python)

## 🏁 Installation et Lancement

1. **Cloner le dépôt :**

   ```bash
   git clone <url-du-depot>
   cd <nom-du-dossier>
   ```

2. **Lancer l'application :**

   ```bash
   python app.py
   ```

## 📖 Utilisation

Au lancement, un menu interactif s'affiche avec les options suivantes :

```
Veuillez sélectionner une des options suivantes :
1) Ajouter un nouveau film.
2) Voir les films à venir.
3) Voir tous les films.
4) Marquer un film comme vu.
5) Voir les films regardés.
6) Ajouter un utilisateur.
7) Rechercher un film.
8) Quitter.
```

### Exemples

#### Ajouter un film

Sélectionnez l'option `1`, puis entrez le titre du film et sa date de sortie au format `jj-mm-AAAA`.

```
Titre du film : Inception
Date de sortie (jj-mm-AAAA) : 21-07-2010
```

#### Rechercher un film

Sélectionnez l'option `7`, puis entrez un terme de recherche partiel.

```
Entrez un titre partiel de film : Incep
```

L'application affichera tous les films dont le titre contient le terme recherché.

## 🗄️ Structure de la Base de Données

L'application utilise trois tables SQLite :

### Table `movies`

| Colonne             | Type    | Description                          |
|---------------------|---------|--------------------------------------|
| `id`                | INTEGER | Clé primaire (auto-incrémentée)      |
| `title`             | TEXT    | Titre du film                        |
| `release_timestamp` | REAL    | Date de sortie (timestamp Unix)      |

### Table `users`

| Colonne    | Type | Description                  |
|------------|------|------------------------------|
| `username` | TEXT | Nom d'utilisateur (clé primaire) |

### Table `watched`

| Colonne         | Type    | Description                              |
|-----------------|---------|------------------------------------------|
| `user_username` | TEXT    | Clé étrangère vers `users(username)`     |
| `movie_id`      | INTEGER | Clé étrangère vers `movies(id)`          |

## 📄 Licence

Ce projet est libre d'utilisation à des fins éducatives et personnelles.
