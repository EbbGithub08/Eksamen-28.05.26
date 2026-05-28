# Setup

Kort guide for å få spillet opp å kjøre.

---

## Krav
- Python 3.10+ (3.11 anbefalt)
- `pip` installert
- Internett (kun hvis du bruker leaderboard via API)

---

## Lokal oppstart
1. Åpne prosjektmappen i terminal.
2. (Valgfritt) Lag virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
3. Installer avhengigheter:
   ```bash
   pip install pygame
   ```
4. Kjør spillet:
   ```bash
   python JumpBoy.py
   ```

---

## Database (kort)
- Spillet bruker et database-API for highscores (`Classes/database.py`).
- Endre `api_base_url` hvis serveren din har annen IP/port.

### SQLite (enkel lokal setup)
- Bruk SQLite i API-et for lokal testing.
- Opprett databasefil og tabell i API-prosjektet, start API-et, og pek spillet mot lokal URL (f.eks. `http://127.0.0.1:5000`).

### MySQL (server)
- Sett opp MySQL på server og opprett database + bruker.
- Konfigurer API-et med MySQL-tilkobling (host, user, password, database).
- Start API-et på serveren og bruk serverens URL i `api_base_url`.

---

## Feilsøking
- `ModuleNotFoundError: pygame` -> kjør `pip install pygame`.
- Leaderboard fungerer ikke -> sjekk at API-serveren kjører og at URL i `api_base_url` er riktig.
