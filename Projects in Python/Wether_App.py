# weather_app.py
import requests
import os

API_KEY = os.getenv("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")  # safer than hardcoding
city = input("Enter city: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

try:
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        print(f"🌤 Weather in {city}: {temp}°C, {desc}")
    else:
        print(f"⚠️ Error: {data.get('message', 'Could not fetch weather')}")

except Exception as e:
    print("⚠️ Request failed:", e)
