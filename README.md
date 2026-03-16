# 🎬 Film Kijklijst App

Een command-line applicatie gebouwd met **Python** en **SQLite** waarmee je een persoonlijke film kijklijst kunt beheren.

## 📖 Beschrijving

Met deze applicatie kun je films toevoegen, bijhouden welke films je hebt bekeken en zoeken naar films in je collectie. De app ondersteunt meerdere gebruikers, zodat iedereen zijn eigen kijkgeschiedenis kan bijhouden.

## ✨ Functionaliteiten

- **Film toevoegen** — Voeg een nieuwe film toe met titel en releasedatum.
- **Aankomende films bekijken** — Bekijk een overzicht van films die nog moeten uitkomen.
- **Alle films bekijken** — Toon een lijst van alle films in de database.
- **Film als bekeken markeren** — Markeer een film als bekeken voor een specifieke gebruiker.
- **Bekeken films bekijken** — Bekijk welke films een gebruiker al heeft gezien.
- **Gebruiker toevoegen** — Voeg een nieuwe gebruiker toe aan de app.
- **Films zoeken** — Zoek naar films op basis van een (gedeeltelijke) titel.

## 🛠️ Technologieën

| Technologie | Doel |
|---|---|
| Python 3 | Programmeertaal |
| SQLite | Database |
| `sqlite3` | Python standaardbibliotheek voor SQLite |
| `datetime` | Datum- en tijdverwerking |

## 📁 Projectstructuur

```
├── app.py          # Hoofdapplicatie met menu en gebruikersinteractie
├── database.py     # Databaselogica en SQL-queries
├── data.db         # SQLite-databasebestand (wordt automatisch aangemaakt)
└── README.md       # Dit bestand
```

## 🚀 Installatie & Gebruik

### Vereisten

- Python 3.6 of hoger

### Starten

1. Kloon de repository:
   ```bash
   git clone <repository-url>
   cd <projectmap>
   ```

2. Start de applicatie:
   ```bash
   python app.py
   ```

3. Volg het menu in de terminal:
   ```
   Selecteer een van de volgende opties:
   1) Nieuwe film toevoegen.
   2) Aankomende films bekijken.
   3) Alle films bekijken.
   4) Film als bekeken markeren.
   5) Bekeken films bekijken.
   6) Gebruiker toevoegen.
   7) Film zoeken.
   8) Afsluiten.
   ```

## 🗄️ Database

De applicatie maakt gebruik van een SQLite-database (`data.db`) met de volgende tabellen:

### `movies`
| Kolom | Type | Beschrijving |
|---|---|---|
| `id` | INTEGER (PK) | Uniek film-ID |
| `title` | TEXT | Titel van de film |
| `release_timestamp` | REAL | Releasedatum als Unix-timestamp |

### `users`
| Kolom | Type | Beschrijving |
|---|---|---|
| `username` | TEXT (PK) | Gebruikersnaam |

### `watched`
| Kolom | Type | Beschrijving |
|---|---|---|
| `user_username` | TEXT (FK) | Verwijzing naar gebruiker |
| `movie_id` | INTEGER (FK) | Verwijzing naar film |

## 📝 Voorbeeld

```
Welkom bij de kijklijst app!

> Keuze: 1
  Film titel: The Matrix
  Releasedatum (dd-mm-JJJJ): 31-03-1999

> Keuze: 6
  Gebruikersnaam: jan

> Keuze: 4
  Gebruikersnaam: jan
  Film ID: 1

> Keuze: 5
  Gebruikersnaam: jan
  -- Bekeken films --
  1: The Matrix (op Mar 31 1999)
```

## 📄 Licentie

Dit project is beschikbaar als open-source.
