import mip
mip.install("dht") 

import dht
import machine
import time

# Use GPIO 4 (D4) for the DHT22 sensor
DHT_PIN = 4
sensor = dht.DHT22(machine.Pin(DHT_PIN))

while True:

    # Current Time 
    current_time = time.localtime()
    formatted_time = f"{current_time[3]:02}:{current_time[4]:02}:{current_time[5]:02}"
    print(f"Current Time: {formatted_time}")

    try:
        sensor.measure()  # Read data
        temp = sensor.temperature()  # Temperature in Celsius
        hum = sensor.humidity()  # Humidity in %
        print(f"Temperature: {temp:.2f} °C, Humidity: {hum:.2f} %")

        # Get Temperature Sensor Reading From Pin 4
        # temp_sensor = machine.ADC(machine.Pin(4))
        # temp_sensor_value = temp_sensor.read_u16()  # Read the ADC value
        # print(f"Raw ADC Value: {temp_sensor_value}")
        # print(f"Temperature Sensor Reading: {temp_sensor_celsius:.2f} °C")
            
    except OSError as e:
        print("❌ Failed to read from DHT22 sensor. Check connections.")

    time.sleep(1)  # Wait 2 seconds before next reading