# This program was created in Arduino Lab for MicroPython
import time
import ntptime
import network

# Wi-Fi Credentials
SSID = "WIFI_SSID"
PASSWORD = "WIFI_PASSWORD"

# Synchronize Time
try:
    print("Syncing time with NTP server...")
    ntptime.settime()  # Syncs with pool.ntp.org
    print("Time synchronized successfully!")
except Exception as e:
    print("Failed to sync time:", e)

# Connect to Wi-Fi
# def connect_wifi():
#     wlan = network.WLAN(network.STA_IF)
#     wlan.active(True)
#     wlan.connect(SSID, PASSWORD)

#     print("Connecting to Wi-Fi", end="")
#     while not wlan.isconnected():
#         print(".", end="")
#         time.sleep(1)
    
#     print("\nWi-Fi Connected!")
#     print("IP Address:", wlan.ifconfig()[0])
  
while True:
  current_time = time.localtime()
  formatted_time = "{:02d}:{:02d}:{:02d}".format(current_time[3], current_time[4], current_time[5])
  print(formatted_time)
  time.sleep(1)