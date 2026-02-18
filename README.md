# Application de Liste de Films à Regarder

Une application de gestion de liste de films développée en Python avec SQLite. Cette application permet de suivre les films que vous souhaitez regarder et ceux que vous avez déjà vus.

## Fonctionnalités

- ✅ Ajouter de nouveaux films à la liste
- 📅 Consulter les films à venir
- 📋 Voir tous les films de la liste
- 👁️ Marquer un film comme regardé
- 📊 Consulter les films regardés par utilisateur
- 👤 Ajouter des utilisateurs à l'application
- 🔍 Rechercher des films par titre

## Prérequis

- Python 3.x
- SQLite3 (généralement inclus avec Python)

## Installation

1. Clonez ce dépôt ou téléchargez les fichiers du projet

2. Assurez-vous d'avoir Python installé sur votre système :
   ```bash
   python --version
   ```

3. Les dépendances nécessaires sont incluses dans la bibliothèque standard de Python (sqlite3, datetime), aucune installation supplémentaire n'est requise.

## Utilisation

1. Lancez l'application :
   ```bash
   python app.py
   ```

2. Suivez les instructions du menu pour naviguer dans l'application :
   - **1** : Ajouter un nouveau film
   - **2** : Voir les films à venir
   - **3** : Voir tous les films
   - **4** : Marquer un film comme regardé
   - **5** : Voir les films regardés par un utilisateur
   - **6** : Ajouter un utilisateur
   - **7** : Rechercher un film
   - **8** : Quitter l'application

## Structure du Projet

- `app.py` : Fichier principal contenant l'interface utilisateur et la logique de l'application
- `database.py` : Module de gestion de la base de données SQLite
- `data.db` : Base de données SQLite (créée automatiquement lors de la première exécution)

## Base de Données

L'application utilise SQLite avec trois tables principales :

- **movies** : Stocke les informations des films (id, titre, date de sortie)
- **users** : Stocke les utilisateurs de l'application
- **watched** : Table de liaison pour suivre les films regardés par chaque utilisateur

## Format de Date

Lors de l'ajout d'un film, utilisez le format de date suivant : `jj-mm-AAAA` (par exemple : `18-02-2026`)

Si aucune date n'est fournie, la date du jour sera utilisée par défaut.

## Exemple d'Utilisation

1. Ajoutez un utilisateur (option 6)
2. Ajoutez quelques films à votre liste (option 1)
3. Consultez les films à venir (option 2)
4. Marquez un film comme regardé (option 4)
5. Consultez vos films regardés (option 5)

## Notes

- La base de données est créée automatiquement lors de la première exécution
- Les données sont persistantes et conservées entre les sessions
- Vous pouvez rechercher des films en utilisant une partie du titre

## Licence

Ce projet est fourni tel quel à des fins éducatives.
