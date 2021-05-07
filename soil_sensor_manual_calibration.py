from time import sleep
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

# In the end this is simply assigning GPIO pin #s to the SPI object.
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# Again, this is is BCM, so board pin 29
cs = digitalio.DigitalInOut(board.D5) #

mcp=MCP.MCP3008(spi,cs)

chan = AnalogIn(mcp, MCP.P0)

print('Manual SPI calibration of soil sensors')
print('')
print('First step: record high voltage')
text = input('Is the sensor completely dry? (Y/n)')
if text == 'Y' or text == 'y':
	# Try some of the calibration coding ideas from this website:
	# https://www.avimesa.com/docs/dev-kits/connecting-analog-sensors-raspberry-pi/
	# (e.g.: sample averaging)
	# ALSO: try avimesa.live graphs from lower part of that webpage
	dry = chan.value
else:
	print('Manual calibration aborted')
	quit()
	
	
print('Straight ADC Value:', chan.value)
print('Straight ADC Voltage:'+ str(chan.voltage))
sleep(5)
print('Straight ADC Value:', chan.value)
print('Straight ADC Voltage:'+ str(chan.voltage))
