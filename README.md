# Időjárás Webalkalmazás

Ez a Python-alapú időjárás-alkalmazás lehetővé teszi a felhasználók számára, hogy lekérdezzék a városok aktuális időjárását és 5 napos előrejelzését. 
Az alkalmazás az OpenWeatherMap API-t használja az időjárási adatok lekérésére, és HTML/CSS segítségével vizualizálja azokat.

## Funkciók

- **Aktuális időjárás** megjelenítése a város neve, hőmérséklet, páratartalom, szélsebesség és csapadék alapján.
- **5 napos időjárás-előrejelzés**, amely tartalmazza a hőmérsékletet, páratartalmat és csapadékot.
- **Grafikus megjelenítés** a Chart.js segítségével, amely a hőmérséklet változását mutatja.
- **Felhasználóbarát HTML felület**, amely tartalmazza az aktuális időjárási adatokat és a részletes előrejelzéseket.

## Telepítés

1. **Python telepítése**: Győződj meg róla, hogy Python 3.x telepítve van a számítógépeden.
   
2. **Követelmények telepítése**: Telepítsd a `requests` könyvtárat a következő parancsokkal:
   ```bash
   pip install requests
API Kulcs: Regisztrálj az OpenWeatherMap weboldalon, és szerezd meg az API kulcsodat. A kódban állítsd be a API_KEY változót a saját kulcsodra.

A program futtatása: Futtasd a következő parancsot a parancssorban:

bash
Kód másolása
python idojaras.py
Város kiválasztása: Add meg a város nevét, amelynek időjárását szeretnéd lekérdezni.

HTML fájl megtekintése: A program futtatása után a idojaras.html fájl generálódik. Nyisd meg ezt a fájlt a böngésződben, hogy megtekintsd az időjárási adatokat és a grafikonokat.
