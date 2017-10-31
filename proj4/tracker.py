import RPi.GPIO as GPIO # import GPIO librery
import time

GPIO.setmode(GPIO.BOARD)

OTD = 16
OTB = 18
OTA = 22
OTC = 40
OTE = 32

#sensor setting
GPIO.setup(OTD,GPIO.IN)
GPIO.setup(OTB,GPIO.IN)
GPIO.setup(OTA,GPIO.IN)
GPIO.setup(OTC,GPIO.IN)
GPIO.setup(OTE,GPIO.IN)

def getLocation():
	#GPIO.input(OTD)==True
	print(GPIO.input(OTD))

if __name__ == '__main__':
	getLocation()
