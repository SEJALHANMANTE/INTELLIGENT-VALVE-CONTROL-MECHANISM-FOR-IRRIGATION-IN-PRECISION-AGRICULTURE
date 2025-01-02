import csv
import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import numpy as np



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
temp = []
try:  
    while True:
        now = time.localtime()
         
        # Check for specific times (8 AM, 1 PM, 6 PM)
        if now.tm_hour in(8, 13, 18) and 0 <= now.tm_min <30 :  # Take readings within first 10 minutes
           

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
                    rain_status ="Not Raining"
                else:
                    rain_status = "Raining"

                if read_moisture_sensor():
                    moisture_value = "DRY"
                else:
                    moisture_value = "WET"

                humidity, temperature = read_dht_sensor()
                temp.append(temperature)
                if rain_status == "Raining":
                    Weather="RAINY"
                elif temperature <= 30 and rain_status == 'Not Raining':
                    Weather = "NORMAL"
                elif temperature >30 :
                    Weather = "SUNNY"
                elif temperature >30 and humidity > 60 and moisture_value=="Wet":
                    moisture_value="HUMID"
                 
                temp1=np.array(temp)
                CROP_TYPE="POTATO"
                REGION = "SEMI ARID"
                current_time = time.strftime('%Y-%m-%d %H:%M:%S')
                if len(temp1)==3:
                    
                    TEMP_MIN = temp1.min() 
                    TEMP_MAX= temp1.max()
                    print(f'Temp_min:{TEMP_MIN}') 
                    print(f'Temp_MAX:{TEMP_MAX}')


                
                    
                    data_to_add=[current_time,CROP_TYPE,moisture_value,REGION,Weather,TEMP_MIN,TEMP_MAX]
                    add_data_to_csv(fPath,data_to_add)
                
                
                
                print(f"Weather: {Weather}")
                print(f"Moisture: {moisture_value}")
               
                print(f'Temp:{temp}')
                print(f"DHT Sensor - Humidity: {humidity}%, Temperature: {temperature}°C")
                print(temp1)

                time.sleep(4*60*60) 
except KeyboardInterrupt:
    print("Script terminated by user.")
finally:
    GPIO.cleanup()



        

