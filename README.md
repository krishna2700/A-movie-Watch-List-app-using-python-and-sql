# Film Watchlist Applicatie

Een eenvoudige command-line applicatie gebouwd met Python en SQLite voor het bijhouden van films die je wilt bekijken en films die je al hebt gezien.

## Functionaliteiten

- **Films toevoegen**: Voeg nieuwe films toe aan je watchlist met titel en releasedatum
- **Aankomende films bekijken**: Bekijk films die nog moeten uitkomen
- **Alle films bekijken**: Toon alle films in de database
- **Films markeren als bekeken**: Markeer films die je hebt gezien
- **Bekeken films bekijken**: Bekijk welke films een gebruiker al heeft gezien
- **Gebruikersbeheer**: Voeg gebruikers toe aan de applicatie
- **Films zoeken**: Zoek films op basis van gedeeltelijke titel

## Vereisten

- Python 3.8 of hoger
- SQLite3 (standaard inbegrepen bij Python)

## Installatie

1. Clone deze repository:
```bash
git clone <repository-url>
cd <repository-map>
```

2. Geen extra packages nodig - gebruikt alleen Python standaard bibliotheken!

## Gebruik

Start de applicatie met:

```bash
python app.py
```

### Menu Opties

Bij het starten van de applicatie krijg je het volgende menu te zien:

```
1) Add new movie - Voeg een nieuwe film toe
2) View upcoming movies - Bekijk aankomende films
3) View all movies - Bekijk alle films
4) Add watched movie - Markeer een film als bekeken
5) View watched movies - Bekijk bekeken films van een gebruiker
6) Add user to the app - Voeg een gebruiker toe
7) Search for a movie - Zoek een film
8) Exit - Afsluiten
```

### Voorbeeldgebruik

1. **Gebruiker toevoegen**: Selecteer optie 6 en voer een gebruikersnaam in
2. **Film toevoegen**: Selecteer optie 1, voer de filmtitel en releasedatum in (formaat: dd-mm-YYYY)
3. **Films bekijken**: Selecteer optie 2 voor aankomende films of optie 3 voor alle films
4. **Film als bekeken markeren**: Selecteer optie 4, voer gebruikersnaam en film-ID in
5. **Bekeken films bekijken**: Selecteer optie 5 en voer de gebruikersnaam in

## Database Structuur

De applicatie gebruikt een SQLite database (`data.db`) met de volgende tabellen:

### Movies (Films)
- `id`: Unieke identificatie (INTEGER PRIMARY KEY)
- `title`: Filmtitel (TEXT)
- `release_timestamp`: Releasedatum als timestamp (REAL)

### Users (Gebruikers)
- `username`: Gebruikersnaam (TEXT PRIMARY KEY)

### Watched (Bekeken)
- `user_username`: Gebruikersnaam (TEXT, FOREIGN KEY)
- `movie_id`: Film-ID (INTEGER, FOREIGN KEY)

## Projectstructuur

```
.
├── app.py          # Hoofdapplicatie met gebruikersinterface
├── database.py     # Database operaties en queries
└── data.db         # SQLite database (wordt automatisch aangemaakt)
```

## Technische Details

- **Programmeertaal**: Python 3
- **Database**: SQLite3
- **Datum handling**: datetime module voor conversie tussen mensleesbare datums en timestamps
- **Database indexering**: Index op release_timestamp voor snellere queries van aankomende films

## Licentie

Dit project is beschikbaar voor educatieve doeleinden.

## Bijdragen

Bijdragen zijn welkom! Voel je vrij om een pull request in te dienen of issues te openen voor bugs en feature requests.
