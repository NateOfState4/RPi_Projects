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


# Set up SPI moisture sensor(s)
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)


cs = digitalio.DigitalInOut(board.D5) # D5=board pin 29

mcp=MCP.MCP3008(spi,cs)

chan = AnalogIn(mcp, MCP.P0)

hum_obs = chan0.value



# Import moisture sensor calibration
sensor1 = 'Soil1'
calib_data = pd.read_csv(sensor1+'.csv')
print calib_data

