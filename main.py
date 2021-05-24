# Tomato Plant Watering
# Nathan Huffman
# 05-2021

import busio
import digitalio
# 'board' is searching for the type of microcontroller (e.g.: RPi 40-pin).
# It then maps all of the pins and gives them initial values (e.g.: LOW).
# board automatically uses BCM!!! (i.e.: D2=GPIO 2=SDA=board pin #3)
import board
# mcp3008 sets up analog input directions and reference voltages.
# Also does some complicated shit to set up SPI. Whatever.
# MCP3008 hardcoded to use 3.3V!!!
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import pandas as pd
import RPi.GPIO as GPIO
import time
from time import sleep
import numpy as np
import datetime
import Adafruit_DHT
import mysql.connector


now = datetime.datetime.now()

# Set up SPI moisture sensor(s)
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.D5) # D5=board pin 29
mcp=MCP.MCP3008(spi,cs)

chan0 = AnalogIn(mcp, MCP.P0)
chan1 = AnalogIn(mcp, MCP.P1)
chan2 = AnalogIn(mcp, MCP.P2)

hum_obs_raw0 = chan0.value
hum_obs_raw1 = chan1.value
hum_obs_raw2 = chan2.value



# Import moisture sensor calibration
sensor0 = 'Soil1'
sensor0_data = pd.read_csv('./calibration_files/'+sensor0+'.csv')
print(sensor0_data)
sensor1 = 'Soil2'
sensor1_data = pd.read_csv('./calibration_files/'+sensor1+'.csv')
print(sensor1_data)
sensor2 = 'Soil3'
sensor2_data = pd.read_csv('./calibration_files/'+sensor2+'.csv')
print(sensor2_data)
print(hum_obs_raw0)
print(hum_obs_raw1)
print(hum_obs_raw2)
# Calibrated 0%-100%
moist0 = (hum_obs_raw0-sensor0_data['b'].iloc[0])/sensor0_data['m'].iloc[0]
moist1 = (hum_obs_raw1-sensor1_data['b'].iloc[0])/sensor1_data['m'].iloc[0]
moist2 = (hum_obs_raw2-sensor2_data['b'].iloc[0])/sensor2_data['m'].iloc[0]
print(str(moist0)+'%')
print(str(moist1)+'%')
print(str(moist2)+'%')
moist_avg = np.mean([moist0,moist1,moist2])

# Need block of code to account for >100% or <0% humidity
#
#
#
#
#
#
#
#
#

# Let's water for 30 seconds in the morning and 
# see how the soil moisture responds

# Set up relay
in1=12
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)

# Boolean for watering
needs_watering = False

# ALGORITHM FOR WATERING
#
# Temperature lock - 100?

# Time lock



if moist_avg < 30.:
	needs_watering = True

# Relay is a normally closed relay
# This means that a low output enables relay
if needs_watering:
	print('Soil moisture is ' + str(moist_avg) + '%')
	print('Watering in progress...')
	GPIO.output(in1,GPIO.LOW)
	time.sleep(30)
	GPIO.output(in1,GPIO.HIGH)
	print('Watering complete!')
	GPIO.cleanup()
else:
	GPIO.cleanup()

# Record temperature and humidity

# BCM pin, not board pin
sensor=Adafruit_DHT.DHT11
sensor_pin1=23
sensor_pin2=24

hum1, tmp1 = Adafruit_DHT.read_retry(sensor,sensor_pin1)
hum2, tmp2 = Adafruit_DHT.read_retry(sensor,sensor_pin2)
tmp1 = tmp1*9./5. + 32.
tmp2 = tmp2*9./5. + 32.



# Record sensor output
conn = mysql.connector.connect(user='nathan',
							database='RoofProject',
							password='eTHrseEb0wot1iC9')
cursor = conn.cursor()

sql = ("""INSERT INTO SENSORS
			(timestamp,
			temperature1,temperature2,
			humidity1,humidity2,
			moisture1,moisture2,moisture3)
			VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""")


	
cursor.execute(sql,(now.strftime("%Y-%m-%d %H:%M"),
					tmp1,tmp2,
					hum1,hum2,
					float(moist0),float(moist1),float(moist2)))

conn.commit()




cursor.close()
conn.close()


