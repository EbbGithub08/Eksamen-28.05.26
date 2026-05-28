# Pygame Platformer

Et 2D platformer-spill laget i **Python med Pygame**.  
Flere verdener, timer, deaths, leaderboard og en ekstra **Demon World**.

---

## Gameplay
- Løp og hopp gjennom levels
- Unngå fiender, lava og spikes
- Fullfør alle levels i en verden for å vinne
- Tiden din blir målt

---

## Verdener
- World 1–3
- Tutorial
- Demon World (egen musikk + leaderboard)

---

## Leaderboard
- Highscores lagres nå via et database-API
- Data sendes til server og hentes per verden
- Top scores vises i menyen
- For nå er Leaderboard funksjonen bare tilgjengelig på på skole ip-en

---

## Database endringer
- Gått fra lokal lagring til API-basert lagring
- Lagrer: brukernavn, world, tid, coins og perfect run
- Brukernavn renses automatisk (kun bokstaver, maks 9 tegn)

---

## Kontroller
- **A / ←** – venstre  
- **D / →** – høyre  
- **W / ↑ / SPACE** – hopp  
- **R** – restart level  
- **ESC** – tilbake / meny  
- **ENTER** – lagre navn etter win  

---

## Teknisk
- Python
- Pygame
- Database API (HTTP + JSON)
- Level-data lagret med pickle

---

## Tools
- level_editor.py
- Ikke laget selv men brukt for å lage nivåene
  
---

## Hvordan kjøre
```bash
pip install pygame
python main.py
```

## Kildeliste
- [Coding With Russ - Platformer Tutorial](https://www.youtube.com/watch?v=Ongc4EVqRjo&list=PLjcN1EyupaQnHM1I9SmiXfbT6aG4ezUvu&index=1)
- Småbruk av KI

## Bilder
![Preview 1](../img/preview1.png)
![Preview 2](../img/preview2.png)
![Preview 3](../img/preview3.png)

