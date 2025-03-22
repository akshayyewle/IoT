# This program was created in Arduino Lab for MicroPython

import network
import urequests
import ujson
import time
import ntptime

# Wi-Fi Credentials
SSID = "WIFI_SSID"
PASSWORD = "WIFI_PASSWORD"

# OpenWeather API Details
API_KEY = "API_KEY"
CITIES = ["London,UK","Cardiff,UK","Mumbai,India"]

# Synchronize Time
try:
    print("Syncing time with NTP server...")
    ntptime.settime()  # Syncs with pool.ntp.org
    print("Time synchronized successfully!")
except Exception as e:
    print("Failed to sync time:", e)

# Connect to Wi-Fi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)

    print("Connecting to Wi-Fi", end="")
    while not wlan.isconnected():
        print(".", end="")
        time.sleep(1)
    
    print("\nWi-Fi Connected!")
    print("IP Address:", wlan.ifconfig()[0])

# Fetch Weather Data
def fetch_weather():
  for CITY in CITIES:
    try:
      API_URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
      response = urequests.get(API_URL)
      weather_data = response.json()
      response.close()

      weather = weather_data["weather"][0]["description"]
      temp = weather_data["main"]["temp"]
      humidity = weather_data["main"]["humidity"]
      location = list(weather_data["coord"].values())
      current_time = time.localtime()
      formatted_time = "{:02d}:{:02d}:{:02d}".format(current_time[3], current_time[4], current_time[5])

      # print("\nWeather Data:")
      print(f"\n{CITY}")
      print(formatted_time)
      print(f"Location Coordiates: {location}")
      print(f"Weather: {weather}")
      print(f"Temperature: {temp}°C")
      print(f"Humidity: {humidity}%")
        
    except Exception as e:
        print("Error fetching weather:", e)

# Main Loop
connect_wifi()
while True:
    fetch_weather()
    time.sleep(60)  # Fetch data every 1 minutes
