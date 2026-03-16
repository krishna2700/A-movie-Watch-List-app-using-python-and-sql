# Film Watchlist Applicatie

Een eenvoudige command-line applicatie gebouwd met Python en SQLite voor het beheren van je persoonlijke film watchlist.

## Beschrijving

Deze applicatie stelt gebruikers in staat om films toe te voegen aan hun watchlist, films te markeren als bekeken, en hun filmcollectie te doorzoeken. De applicatie gebruikt een SQLite database om alle gebruikers, films en bekijkhistorie op te slaan.

## Functies

- **Films toevoegen**: Voeg nieuwe films toe met een titel en releasedatum
- **Aankomende films bekijken**: Bekijk films die nog moeten uitkomen
- **Alle films bekijken**: Toon een volledig overzicht van alle films in de database
- **Film als bekeken markeren**: Markeer films die je hebt bekeken
- **Bekeken films bekijken**: Bekijk de lijst met films die een specifieke gebruiker heeft bekeken
- **Gebruikers toevoegen**: Voeg nieuwe gebruikers toe aan de applicatie
- **Films zoeken**: Zoek films op basis van een gedeeltelijke titel
- **Database indexering**: Geoptimaliseerde queries voor releasedatums

## Vereisten

- Python 3.8 of hoger
- SQLite3 (meestal standaard meegeleverd met Python)

## Installatie

1. Clone deze repository:
```bash
git clone <repository-url>
cd <repository-directory>
```

2. De applicatie gebruikt alleen Python standaard bibliotheken, dus er zijn geen extra dependencies om te installeren.

## Gebruik

Start de applicatie met het volgende commando:

```bash
python app.py
```

### Menu Opties

Bij het starten van de applicatie krijg je het volgende menu te zien:

```
1) Add new movie       - Voeg een nieuwe film toe aan de database
2) View upcoming movies - Bekijk films die in de toekomst uitkomen
3) View all movies     - Bekijk alle films in de database
4) Add watched movie   - Markeer een film als bekeken door een gebruiker
5) View watched movies - Bekijk de bekeken films van een gebruiker
6) Add user to the app - Voeg een nieuwe gebruiker toe
7) Search for a movie  - Zoek naar films op titel
8) Exit                - Sluit de applicatie af
```

### Voorbeeldgebruik

**Een film toevoegen:**
1. Selecteer optie `1`
2. Voer de filmtitel in
3. Voer de releasedatum in (formaat: dd-mm-YYYY) of druk op Enter voor de huidige datum

**Een gebruiker toevoegen:**
1. Selecteer optie `6`
2. Voer een gebruikersnaam in

**Een film als bekeken markeren:**
1. Selecteer optie `4`
2. Voer de gebruikersnaam in
3. Voer het film-ID in (te vinden via optie 3)

## Database Structuur

De applicatie gebruikt drie tabellen:

### movies
- `id` (INTEGER PRIMARY KEY): Unieke film-ID
- `title` (TEXT): Filmtitel
- `release_timestamp` (REAL): Releasedatum als timestamp

### users
- `username` (TEXT PRIMARY KEY): Unieke gebruikersnaam

### watched
- `user_username` (TEXT): Verwijzing naar gebruiker
- `movie_id` (INTEGER): Verwijzing naar film
- Foreign keys naar users en movies tabellen

## Bestandsstructuur

```
.
├── app.py          # Hoofd applicatie met menu en gebruikersinterface
├── database.py     # Database functionaliteit en SQL queries
├── data.db         # SQLite database bestand (wordt automatisch aangemaakt)
└── README.md       # Deze documentatie
```

## Technische Details

- **Database**: SQLite3
- **Datum formaat**: Timestamps voor opslag, dd-mm-YYYY voor gebruikersinvoer
- **Database Connectie**: Persistent connection gedurende de applicatie sessie
- **Indexering**: Index op release_timestamp voor snellere queries

## Licentie

Dit project is open source en beschikbaar voor educatieve doeleinden.
