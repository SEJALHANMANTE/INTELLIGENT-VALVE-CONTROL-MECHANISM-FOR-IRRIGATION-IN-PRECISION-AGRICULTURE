import csv
import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = 'Put your credentials here'
firebase_admin.initialize_app(cred, {
    'databaseURL': ''  # Replace with your database URL
})
ref = db.reference('/sensors_readings')
def send_data_to_firebase(data):
    ref.push().set(data)

fPath='data.csv'

GPIO.setmode(GPIO.BCM)

DHT_SENSOR = Adafruit_DHT.DHT11

rainSensorPin = 21
moistureSensorPin = 20
dhtSensorPin = 16

GPIO.setup(rainSensorPin, GPIO.IN)
GPIO.setup(moistureSensorPin, GPIO.IN)

def read_rain_sensor():
    return GPIO.input(rainSensorPin)

def read_moisture_sensor():
    return GPIO.input(moistureSensorPin)

def read_dht_sensor():
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, dhtSensorPin)
    return humidity, temperature

def add_data_to_csv(fPath,data): 
    with open(fPath,'a',newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(data)

try:  
    while True:
        now = time.localtime()
        # Check for specific times (8 AM, 1 PM, 6 PM)
        if now.tm_hour in (8, 11, 18) and 0 <= now.tm_min < 14:  # Take readings within first 10 minutes
            

        # Adjust sleep time to avoid unnecessary readings (approximately 4 hours)
                 # Sleep for 4 hours
                def read_rain_sensor():
                    return GPIO.input(rainSensorPin)

                def read_moisture_sensor():
                    return GPIO.input(moistureSensorPin)

                def read_dht_sensor():
                    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, dhtSensorPin)
                    return humidity, temperature

                def add_data_to_csv(fPath,data): 
                    with open(fPath,'a',newline='') as csv_file:
                        writer = csv.writer(csv_file)
                        writer.writerow(data)
                if read_rain_sensor():
                    rain_status = "Not Raining"
                else:
                    rain_status = "Raining"

                if read_moisture_sensor():
                    moisture_value = "DRY"
                else:
                    moisture_value = "WET"

                humidity, temperature = read_dht_sensor()
                
                if rain_status == "Raining":
                    Weather="RAINY"
                elif temperature <= 30 and rain_status == 'Not Raining':
                    Weather = "NORMAL"
                elif temperature >30 :
                    Weather = "SUNNY"
                elif temperature >30 and humidity > 60 and moisture_value=="Wet":
                    moisture_value="HUMID"
                 
                
                CROP_TYPE="POTATO"
                REGION = "SEMI ARID"
                TEMP_MIN = 18 
                TEMP_MAX= 35


                
                current_time = time.strftime('%Y-%m-%d %H:%M:%S')
                data_to_add=[current_time,CROP_TYPE,moisture_value,REGION,Weather,TEMP_MIN,TEMP_MAX]
                add_data_to_csv(fPath,data_to_add)
                
                data_to_send = {
                    'current time':current_time,
                    'crop type':CROP_TYPE,
                    'moisture':moisture_value,
                    'min_temperature': TEMP_MIN,
                    'MAX_TEMP':TEMP_MAX,
                    'humidity': humidity     # Replace with your actual data
                }
                send_data_to_firebase(data_to_send)
                print("Data sent to Firebase")
                
                print(f"Time: {current_time}")
                print(f"Weather: {Weather}")
                print(f"Moisture: {moisture_value}")
                print(f'Temp_min:{TEMP_MIN}')
                print(f'Temp_MAX:{TEMP_MAX}')
                print(f"DHT Sensor - Humidity: {humidity}%, Temperature: {temperature}°C")
                print()

                time.sleep(4 * 60 * 60) 
except KeyboardInterrupt:
    print("Script terminated by user.")
finally:
    GPIO.cleanup()


print("Done")