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
import os
import pandas as pd
import json

# In the end this is simply assigning GPIO pin #s to the SPI object.
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# Again, this is is BCM, so board pin 29
cs = digitalio.DigitalInOut(board.D5) #

mcp=MCP.MCP3008(spi,cs)

chan = AnalogIn(mcp, MCP.P2)

print('Manual SPI calibration of soil sensors')
sensor_name = input('Enter name of sensor (e.g.: Soil2, Temp1)')
print('')
print('First step: record high voltage')
text = input('Is the sensor completely dry? (Y/n)')
if text == 'Y' or text == 'y':
	# Try some of the calibration coding ideas from this website:
	# https://www.avimesa.com/docs/dev-kits/connecting-analog-sensors-raspberry-pi/
	# (e.g.: sample averaging...maybe try next highest reading instead?)
	# ALSO: try avimesa.live graphs from lower part of that webpage
	dry = chan.value
else:
	print('Manual calibration aborted')
	quit()
	

print('Second step: record low voltage')
text = input('Is the sensor submerged in water? (Y/n)')
if text == 'Y' or text == 'y':
	wet = chan.value
else:
	print('Manual calibration aborted')
	quit()

# y=mx+b
m = (wet-dry)/(100.-0.)
b = dry-m*0.

# For now, let's write this to a csv using pandas
df = pd.DataFrame([[dry,wet,m,b]],
					columns=['MaxValue','MinValue','m','b'])
filename=sensor_name+'.csv'

print(df)

print('')
text = input('Keep these results? (Y/n)')
if text == 'Y' or text == 'y':
	print('Calbration successful')
	with open('./calibration_files/'+filename,"w") as myfile:
		data = df.to_csv(index=False)
		myfile.write(data)
else:
	print('Manual calibration aborted')
	quit()
