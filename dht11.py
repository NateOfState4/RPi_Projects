import os
import time
import Adafruit_DHT

# BCM pin, not board pin
sensor=Adafruit_DHT.DHT11
sensor_pin1=27
sensor_pin2=22

		
try:
	filename='/home/nathan/RPi_Projects/dht11.csv'
	f = open(filename,'a+')
	if os.stat(filename).st_size == 0:
		f.write('Date,Time,Temperature,Humidity\r\n')

except:
	pass
	
while True:
	hum1, tmp1 = Adafruit_DHT.read_retry(sensor,sensor_pin1)
	hum2, tmp2 = Adafruit_DHT.read_retry(sensor,sensor_pin2)
	print(tmp1, hum1, tmp2, hum2)
	if hum1 is not None and tmp1 is not None and hum2 is not None and tmp2 is not None:
		f.write('{0},{1},{2:0.1f},{3:0.1f}%,{4:0.1f},{5:0.1f}%\r\n'.format(time.strftime('%m/%d/%y'),
		 time.strftime('%H:%M'),tmp1*9./5.+32.,hum1,tmp2*9./5.+32.,hum2))
	else:
		print('Failed to retreive data from sensor')
		
	time.sleep(10)
