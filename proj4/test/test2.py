import RPi.GPIO as GPIO
from time import sleep

class t:
	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(False)



	#const variable	
	MOTOR_LEFT_A = 12
	MOTOR_LEFT_B = 11
	MOTOR_LEFT_PWM = 35

	MOTOR_RIGHT_A = 15
	MOTOR_RIGHT_B = 13
	MOTOR_RIGHT_PWM = 37


	#base setting
	GPIO.setup(MOTOR_LEFT_A, GPIO.OUT)#set left motor pin to output
	GPIO.setup(MOTOR_LEFT_B, GPIO.OUT)
	GPIO.setup(MOTOR_LEFT_PWM, GPIO.OUT)

	GPIO.setup(MOTOR_RIGHT_A, GPIO.OUT)#set right moto pin to output
	GPIO.setup(MOTOR_RIGHT_B, GPIO.OUT)
	GPIO.setup(MOTOR_RIGHT_PWM, GPIO.OUT)

	LeftPwm=GPIO.PWM(MOTOR_LEFT_PWM, 100)#create PWM
	RightPwm=GPIO.PWM(MOTOR_RIGHT_PWM, 100)
	#

	def initial(self):
		self.LeftPwm.start(0)
	def p(self):
		GPIO.output(self.MOTOR_LEFT_A, True)#revered
		GPIO.output(self.MOTOR_LEFT_B, False)

	def q(self):
		GPIO.output(self.MOTOR_LEFT_PWM, GPIO.HIGH)
		self.LeftPwm.ChangeDutyCycle(20)

	def r(self):
		GPIO.output(self.MOTOR_LEFT_PWM, GPIO.LOW)

	def k(self):
		self.initial()
		self.p()
		self.q()
		sleep(1)
		self.r()
'''a=t()
a.p()
a.q()
sleep(1)
a.r()
print("end")
'''

#
'''#public method
def go(leftDirection, rightDirection, leftSpeed, rightSpeed, duration):
	setDirection(leftDirection, rightDirection)#set direction
	setSpeed(leftSpeed, rightSpeed)#set speed
	sleep(duration)#set duration time
        print("here")
		
#private method
def setDirection(leftDirection, rightDirection):
	GPIO.output(MOTOR_LEFT_A, GPIO.HIGH)#not leftDirection)#left motor
	GPIO.output(MOTOR_LEFT_B, GPIO.LOW)

	GPIO.output(MOTOR_RIGHT_A, rightDirection)#right motor
	GPIO.output(MOTOR_RIGHT_B, not rightDirection)

def setSpeed(leftSpeed, rightSpeed):
	LeftPwm.ChangeDutyCycle(leftSpeed)
	RightPwm.ChangeDutyCycle(rightSpeed)
		

go(True, True, 40, 40, 3)
go(True, True, 0, 0, 1)
'''

















