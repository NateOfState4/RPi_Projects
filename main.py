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


# Set up SPI moisture sensor(s)
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)


cs = digitalio.DigitalInOut(board.D5) # D5=board pin 29

mcp=MCP.MCP3008(spi,cs)

chan = AnalogIn(mcp, MCP.P0)

hum_obs_raw = chan.value



# Import moisture sensor calibration
sensor1 = 'Soil1'
sensor1_data = pd.read_csv('./calibration_files/'+sensor1+'.csv')
print(sensor1_data)
print(hum_obs_raw)
# Calibrated 0%-100%
soil1_value = (hum_obs_raw-sensor1_data['b'].iloc[0])/sensor1_data['m'].iloc[0]
print(str(soil1_value)+'%')

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

# Set up relay on 
in1=6
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)

# Boolean for watering
needs_watering = False

if soil1_value < 50.:
	needs_watering = True

# Relay is a normally closed relay
# This means that a low output enables relay
if needs_watering:
	GPIO.output(in1,GPIO.LOW)
	time.sleep(30)
	GPIO.output(in1,GPIO.HIGH)
	GPIO.cleanup()
else:
	GPIO.cleanup()


