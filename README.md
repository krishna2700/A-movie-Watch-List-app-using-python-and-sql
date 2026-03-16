# 🎬 Film Kijklijst App

Een command-line applicatie gebouwd met **Python** en **SQLite** waarmee je een persoonlijke film kijklijst kunt beheren.

## 📖 Beschrijving

Met deze applicatie kun je films toevoegen, bijhouden welke films je hebt bekeken en zoeken naar films in je collectie. De app ondersteunt meerdere gebruikers, zodat iedereen zijn eigen kijklijst kan bijhouden.

## ✨ Functionaliteiten

- **Film toevoegen** — Voeg een nieuwe film toe met titel en releasedatum.
- **Aankomende films bekijken** — Bekijk een overzicht van films die nog moeten uitkomen.
- **Alle films bekijken** — Toon een lijst van alle opgeslagen films.
- **Film als bekeken markeren** — Markeer een film als bekeken voor een specifieke gebruiker.
- **Bekeken films bekijken** — Bekijk welke films een gebruiker al heeft gezien.
- **Gebruiker toevoegen** — Voeg een nieuwe gebruiker toe aan de app.
- **Films zoeken** — Zoek naar films op basis van een (gedeeltelijke) titel.

## 🛠️ Technologieën

| Technologie | Doel |
|---|---|
| Python 3 | Programmeertaal |
| SQLite | Database voor gegevensopslag |

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

1. Clone de repository:
   ```bash
   git clone <repository-url>
   cd <projectmap>
   ```

2. Start de applicatie:
   ```bash
   python app.py
   ```

3. Je wordt begroet met het volgende menu:
   ```
   Welkom bij de kijklijst app!

   Selecteer een van de volgende opties:
   1) Nieuwe film toevoegen.
   2) Aankomende films bekijken.
   3) Alle films bekijken.
   4) Bekeken film toevoegen.
   5) Bekeken films bekijken.
   6) Gebruiker toevoegen.
   7) Zoeken naar een film.
   8) Afsluiten.
   ```

## 💾 Database

De applicatie maakt gebruik van een SQLite-database (`data.db`) met de volgende tabellen:

### Tabellen

- **movies** — Slaat films op met een uniek ID, titel en releasedatum (als timestamp).
- **users** — Slaat gebruikersnamen op.
- **watched** — Koppeltabel die bijhoudt welke gebruiker welke film heeft bekeken.

### Relaties

```
users (username) ──┐
                   ├──> watched (user_username, movie_id)
movies (id) ───────┘
```

## 📝 Voorbeeldgebruik

### Een film toevoegen
```
Kies optie: 1
Filmtitel: The Matrix
Releasedatum (dd-mm-JJJJ): 31-03-1999
```

### Een gebruiker toevoegen
```
Kies optie: 6
Gebruikersnaam: jan
```

### Een film als bekeken markeren
```
Kies optie: 4
Gebruikersnaam: jan
Film ID: 1
```

### Zoeken naar een film
```
Kies optie: 7
Voer (gedeeltelijke) filmtitel in: matrix
```

## 📄 Licentie

Dit project is beschikbaar als open-source.
