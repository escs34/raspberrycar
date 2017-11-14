import RPi.GPIO as GPIO
from time import sleep

class PPicar:
	#const variable	
	MOTOR_LEFT_A = 12
	MOTOR_LEFT_B = 11
	MOTOR_LEFT_PWM = 35

	MOTOR_RIGHT_A = 15
	MOTOR_RIGHT_B = 13
	MOTOR_RIGHT_PWM = 37


	#base setting
	GPIO.setwarnings(False)

	GPIO.setup(MOTOR_LEFT_A, GPIO.out)#set left motor pin to output
	GPIO.setup(MOTOR_LEFT_B, GPIO.out)
	GPIO.setup(MOTOR_LEFT_PWM, GPIO.out)

	GPIO.setup(MOTOR_RIGHT_A, GPIO.out)#set right moto pin to output
	GPIO.setup(MOTOR_RIGHT_B, GPIO.out)
	GPIO.setup(MOTOR_RIGHT_PWM, GPIO.out)

	LeftPwm=GPIO.PWM(MOTOR_LEFT_PWM, 100)#create PWM
	RightPwm=GPIO.PWM(MOTOR_RIGHT_PWM, 100)
	
	#constructor
	def __init__(self):
		print("vroom!")

	#public method
	def go(leftDirection, rightDirection, leftSpeed, rightSpeed, duration_time):
		setDirection(leftDirection, rightDirection)#set direction
		setSpeed(leftSpeed, rightSpeed)#set speed
		sleep(duration_time)#set duration time
	
	#getter
	#empty



	#private method
	def REVERSE(x):
		return not x

	def setDirection(leftDirection, rightDirection):
		GPIO.output(MOTOR_LEFT_A, not leftDirection)#left motor
		GPIO.output(MOTOR_LEFT_B, leftDirection)

		GPIO.output(MOTOR_RIGHT_A, rightDirection)#right motor
		GPIO.output(MOTOR_RIGHT_B, not rightDirection)

	def setSpeed(leftSpeed, rightSpeed):
		LeftPwm.ChangeDutyCycle(leftSpeed)
		RightPwm.ChangeDutyCycle(rightSpeed)




















