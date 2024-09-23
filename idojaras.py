import requests
import json

API_KEY = 'API_KEY'
CITY = input("Add meg a város nevét (pl. Budapest): ")

def fetch_weather_data(city):
    current_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=hu'
    forecast_url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric&lang=hu'
    
    # Lekérjük az aktuális időjárást
    current_response = requests.get(current_url)
    forecast_response = requests.get(forecast_url)

    if current_response.status_code == 200 and forecast_response.status_code == 200:
        current_weather = current_response.json()
        forecast = forecast_response.json()
        return current_weather, forecast
    else:
        return None, None

# Új adatok lekérése az API-tól
current_weather, forecast = fetch_weather_data(CITY)

if current_weather and forecast:
    # Jelenlegi időjárás lekérdezése
    wind_speed = current_weather['wind']['speed'] * 3.6
    icon_code = current_weather['weather'][0]['icon']
    icon_url = f'http://openweathermap.org/img/wn/{icon_code}@2x.png'  

    # HTML tartalom generálása
    html_content = f"""
    <!DOCTYPE html>
    <html lang="hu">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Időjárás - {current_weather['name']}</title>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <style>
            body {{ 
                font-family: 'Arial', sans-serif; 
                background-color: #f4f4f4; 
                color: #333; 
                margin: 0; 
                padding: 20px; 
            }}
            .container {{ 
                max-width: 600px; 
                margin: 0 auto; 
                padding: 20px; 
                background: white; 
                border-radius: 10px; 
                box-shadow: 0 2px 10px rgba(0,0,0,0.1); 
            }}
            h1 {{ 
                text-align: center; 
                color: #007BFF; 
            }}
            img {{ 
                display: block; 
                margin: 0 auto; 
                max-width: 100px; 
            }}
            #myChart {{ 
                max-width: 100%; 
                height: 300px; 
                margin-top: 20px; 
            }}
            .details {{ 
                margin-top: 20px; 
                padding: 10px; 
                background-color: #e9ecef; 
                border-radius: 5px; 
            }}
            ul {{ 
                list-style-type: none; 
                padding: 0; 
            }}
            li {{ 
                padding: 5px 0; 
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Jelenlegi időjárás: {current_weather['name']} ({current_weather['sys']['country']})</h1>
            <img src="{icon_url}" alt="Weather icon">
            <p>Hőmérséklet: {current_weather['main']['temp']} °C</p>
            <p>Páratartalom: {current_weather['main']['humidity']}%</p>
            <p>Csapadék: {current_weather.get('rain', {}).get('1h', 0)} mm</p>
            <p>Szél sebessége: {wind_speed:.2f} km/h</p>

            <canvas id="myChart"></canvas>
            <h2>5 Napos Előrejelzés</h2>
            <div class="details">
                <h3>Részletek</h3>
                <ul>
    """

    # Előrejelzési adatok részletezése
    forecast_dates = []
    temperatures = []
    for day in forecast['list']:
        date_time = day['dt_txt']
        date_parts = date_time.split(" ")
        date = date_parts[0].split("-")
        hour = date_parts[1].split(":")[0]  
        forecast_dates.append(f"{date[1]}.{date[2]}. {hour} óra")  
        temp = day['main']['temp']
        humidity = day['main']['humidity']
        rain = day.get('rain', {}).get('1h', 0)
        temperatures.append(temp)

        html_content += f"<li>{forecast_dates[-1]}: Hőmérséklet: {temp} °C, Páratartalom: {humidity}%, Csapadék: {rain} mm</li>"

    html_content += """
                </ul>
            </div>
        </div>

        <script>
            var ctx = document.getElementById('myChart').getContext('2d');
            var myChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: """ + json.dumps([f"{hour.split(':')[0]}" for hour in forecast_dates]) + """,
                    datasets: [{
                        label: 'Hőmérséklet °C',
                        data: """ + json.dumps(temperatures) + """,
                        borderColor: 'rgba(75, 192, 192, 1)',
                        borderWidth: 2,
                        fill: false
                    }]
                },
                options: {
                    responsive: true,
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
        </script>
    </body>
    </html>
    """

    # HTML fájl létrehozása
    with open('idojaras.html', 'w', encoding='utf-8') as file:
        file.write(html_content)

    print("HTML fájl létrehozva: idojaras.html")
else:
    print("Hiba történt az adatok lekérésekor.")
