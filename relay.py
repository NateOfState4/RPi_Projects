import RPi.GPIO as GPIO
import time

in1=29
in2=31
in3=33
in4=35

GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)

#Relay is a normally closed relay
#This means that a low output enables relay
try:
	while True:
		GPIO.output(in1,GPIO.LOW)
		GPIO.output(in2,GPIO.HIGH)
		GPIO.output(in3,GPIO.HIGH)
		GPIO.output(in4,GPIO.HIGH)
		
except KeyboardInterrupt:
	GPIO.cleanup()
