from sense_hat import SenseHat  
import time  
import sys
import csv
from datetime import datetime
#from ISStreamer.Streamer import Streamer  
#from influxdb import InfluxDBClient
  
# --------- User Settings ---------
CITY = "Nashville"
BUCKET_NAME = ":partly_sunny: " + CITY + " Weather"
BUCKET_KEY = "sensehat"
ACCESS_KEY = "Your_Access_Key"
SENSOR_LOCATION_NAME = "Matt's Room"
MINUTES_BETWEEN_SENSEHAT_READS = 0.1
# ---------------------------------

#streamer = Streamer(bucket_name=BUCKET_NAME, bucket_key=BUCKET_KEY, access_key=ACCESS_KEY)
  
sense = SenseHat()  
  
while True:
  # Read the sensors
  temp_c = sense.get_temperature()
  humidity = sense.get_humidity() 
  pressure_mb = sense.get_pressure() 

  # Format the data
  temp_f = temp_c * 9.0 / 5.0 + 32.0
  temp_f = float("{0:.2f}".format(temp_f))
  humidity = float("{0:.2f}".format(humidity))
  pressure_in = 0.03937008*(pressure_mb)
  pressure_in = float("{0:.2f}".format(pressure_in))
  now = datetime.now()
  dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

  # Print and stream 
  print SENSOR_LOCATION_NAME + " Temperature(F): " + str(temp_f)
  print SENSOR_LOCATION_NAME + " Humidity(%): " + str(humidity)
  print SENSOR_LOCATION_NAME + " Pressure(IN): " + str(pressure_in)
  with open("/home/pi/wunderground-sensehat/weather_record.csv", "a") as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow([dt_string,temp_f,humidity,pressure_in])
  #streamer.log(":sunny: " + SENSOR_LOCATION_NAME + " Temperature(F)", temp_f)
  #streamer.log(":sweat_drops: " + SENSOR_LOCATION_NAME + " Humidity(%)", humidity)
  #streamer.log(":cloud: " + SENSOR_LOCATION_NAME + " Pressure(IN)", pressure_in)

  #streamer.flush()
  time.sleep(60*10)
