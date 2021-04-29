import os
import time
import Adafruit_DHT

# BCM pin, not board pin
sensor=Adafruit_DHT.DHT11
sensor_pin=17

		
try:
	filename='/home/nathan/Python/dht11.csv'
	f = open(filename,'a+')
	if os.stat(filename).st_size == 0:
		f.write('Date,Time,Temperature,Humidity\r\n')

except:
	pass
	
while True:
	hum, tmp = Adafruit_DHT.read_retry(sensor,sensor_pin)
	
	if hum is not None and tmp is not None:
		f.write('{0},{1},{2:0.1f},{3:0.1f}%\r\n'.format(time.strftime('%m/%d/%y'), time.strftime('%H:%M'),tmp*9./5.+32.,hum))
	else:
		print('Failed to retreive data from sensor')
		
	time.sleep(10)
