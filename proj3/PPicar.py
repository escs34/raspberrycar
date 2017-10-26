import RPi.GPIO as GPIO
from time import sleep

class PPicar:
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
	
	#constructor
	def __init__(self):
		self.LeftPwm.start(0)
		self.RightPwm.start(0)
		print("PPika!")

        #public method
	def go(self, leftDirection, rightDirection, leftSpeed, rightSpeed, duration):
		self.setDirection(leftDirection, rightDirection)#set direction
		self.setSpeed(leftSpeed, rightSpeed)#set speed
		sleep(duration)#set duration time
                print("here")
		
	#private method
	def REVERSE(self,x):
		return not x

	def setDirection(self, leftDirection, rightDirection):
		GPIO.output(self.MOTOR_LEFT_A, not leftDirection)#left motor
		GPIO.output(self.MOTOR_LEFT_B, leftDirection)

		GPIO.output(self.MOTOR_RIGHT_A, rightDirection)#right motor
		GPIO.output(self.MOTOR_RIGHT_B, not rightDirection)

	def setSpeed(self, leftSpeed, rightSpeed):
		self.LeftPwm.ChangeDutyCycle(leftSpeed)
		self.RightPwm.ChangeDutyCycle(rightSpeed)
		

















