# Application de Liste de Films à Regarder

Une application en ligne de commande pour gérer votre liste de films à regarder, construite avec Python et SQLite.

## Description

Cette application vous permet de suivre les films que vous souhaitez regarder et ceux que vous avez déjà vus. Elle offre une interface simple en ligne de commande pour gérer votre collection de films personnelle.

## Fonctionnalités

- **Ajouter des films** : Ajoutez de nouveaux films avec leur titre et date de sortie
- **Voir les films à venir** : Consultez les films dont la date de sortie est dans le futur
- **Voir tous les films** : Affichez l'ensemble de votre collection de films
- **Marquer les films comme vus** : Enregistrez les films que vous avez regardés
- **Voir les films vus** : Consultez l'historique des films regardés par utilisateur
- **Gestion des utilisateurs** : Ajoutez plusieurs utilisateurs à l'application
- **Recherche de films** : Recherchez des films par titre partiel

## Prérequis

- Python 3.8 ou supérieur
- SQLite3 (généralement inclus avec Python)

## Installation

1. Clonez ce dépôt :
```bash
git clone <url-du-dépôt>
cd <nom-du-dossier>
```

2. Aucune dépendance externe n'est requise, l'application utilise uniquement des bibliothèques Python standard.

## Utilisation

Lancez l'application en exécutant :

```bash
python app.py
```

### Menu Principal

L'application présente un menu interactif avec les options suivantes :

1. **Ajouter un nouveau film** : Saisissez le titre et la date de sortie (format : jj-mm-AAAA)
2. **Voir les films à venir** : Affiche tous les films avec une date de sortie future
3. **Voir tous les films** : Liste complète de tous les films de la base de données
4. **Ajouter un film vu** : Marquez un film comme vu pour un utilisateur spécifique
5. **Voir les films vus** : Affiche les films regardés par un utilisateur
6. **Ajouter un utilisateur** : Créez un nouveau profil utilisateur
7. **Rechercher un film** : Trouvez des films par recherche partielle de titre
8. **Quitter** : Ferme l'application

### Exemples d'Utilisation

**Ajouter un nouveau film :**
```
Titre du film : Inception
Date de sortie (jj-mm-AAAA) : 16-07-2010
```

**Marquer un film comme vu :**
```
Nom d'utilisateur : alice
ID du film : 1
```

**Rechercher un film :**
```
Entrez un titre partiel : incep
```

## Structure de la Base de Données

L'application utilise SQLite avec trois tables principales :

- **movies** : Stocke les informations des films (ID, titre, horodatage de sortie)
- **users** : Gère les profils utilisateurs (nom d'utilisateur)
- **watched** : Table de liaison entre utilisateurs et films vus

## Structure du Projet

```
.
├── app.py          # Application principale avec l'interface utilisateur
├── database.py     # Gestion de la base de données et requêtes SQL
├── data.db         # Base de données SQLite (créée automatiquement)
└── README.md       # Ce fichier
```

## Caractéristiques Techniques

- Base de données SQLite pour le stockage persistant
- Gestion des dates avec conversion timestamp
- Index sur les dates de sortie pour des performances optimales
- Gestion des clés étrangères pour l'intégrité des données
- Interface en ligne de commande interactive

## Licence

Ce projet est open source et disponible sous licence libre.

## Contributions

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou soumettre une pull request.
