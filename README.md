# Film Watchlist Applicatie

Een eenvoudige command-line applicatie gebouwd met Python en SQLite voor het beheren van je persoonlijke film watchlist.

## Beschrijving

Deze applicatie stelt je in staat om:
- Films toe te voegen aan je watchlist met een releasedatum
- Aankomende films te bekijken
- Alle films in de database te bekijken
- Films te markeren als bekeken
- Bekeken films per gebruiker te raadplegen
- Gebruikers toe te voegen aan de applicatie
- Te zoeken naar films op basis van titels

## Functies

- **Film toevoegen**: Voeg nieuwe films toe met titel en releasedatum
- **Aankomende films**: Bekijk films die na vandaag uitkomen
- **Alle films**: Overzicht van alle films in de database
- **Film als bekeken markeren**: Registreer welke gebruiker welke film heeft bekeken
- **Bekeken films**: Toon alle bekeken films per gebruiker
- **Gebruikersbeheer**: Voeg gebruikers toe aan de applicatie
- **Zoekfunctie**: Zoek films op gedeeltelijke titels
- **Database indexering**: Optimale prestaties door indexering op releasedatum

## Technische Details

### Bestandsstructuur

- `app.py` - Hoofdapplicatie met gebruikersinterface
- `database.py` - Database-logica en SQL-queries
- `data.db` - SQLite database bestand

### Database Schema

De applicatie gebruikt drie tabellen:

1. **movies**: Bevat film-informatie (id, titel, release_timestamp)
2. **users**: Gebruikersinformatie (username)
3. **watched**: Koppeltabel tussen gebruikers en bekeken films

## Installatie

### Vereisten

- Python 3.8 of hoger
- SQLite3 (standaard meegeleverd met Python)

### Stappen

1. Clone de repository:
```bash
git clone <repository-url>
cd <repository-directory>
```

2. De applicatie heeft geen externe dependencies, dus je kunt deze direct uitvoeren.

## Gebruik

Start de applicatie met:

```bash
python app.py
```

### Menu opties

Wanneer de applicatie draait, krijg je het volgende menu te zien:

```
1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Add watched movie
5) View watched movies.
6) Add user to the app.
7) Search for a movie.
8) Exit.
```

### Voorbeeldgebruik

1. **Gebruiker toevoegen** (optie 6):
   - Voer een gebruikersnaam in

2. **Film toevoegen** (optie 1):
   - Voer de filmtitel in
   - Voer de releasedatum in (formaat: dd-mm-YYYY)
   - Als je geen datum invoert, wordt de huidige datum gebruikt

3. **Film als bekeken markeren** (optie 4):
   - Voer de gebruikersnaam in
   - Voer het film-ID in (te vinden in de filmlijst)

4. **Bekeken films bekijken** (optie 5):
   - Voer de gebruikersnaam in
   - Bekijk alle films die deze gebruiker heeft bekeken

## Datumformaat

De applicatie gebruikt het formaat **dd-mm-YYYY** voor datums (bijv. 25-12-2026).

## Database

De applicatie maakt automatisch de benodigde tabellen en indexen aan bij de eerste start. Alle gegevens worden opgeslagen in het bestand `data.db`.

## Licentie

Dit project is open source en beschikbaar voor educatieve doeleinden.
