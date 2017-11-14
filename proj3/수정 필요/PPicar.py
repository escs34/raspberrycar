'''자동차의 기본 기능을 구현해놓은 car 모듈 입니다. Motor Driver에 검은 선이 위, 붉은 선이 아래인 형태입니다.
	예시로 올라온 코드와의 차이점
	1.방향에 True, False값을 직접 넣어주기에 REVERSE함수가 필요없다.
	2.마찬가지 이유로 방향을 저장해두는 변수인 forward0,1 , backward0,1또한 필요없다.
	3.오른쪽 모터와 왼쪽 모터의 방향을 한번에 정하기에 rightmotor와 leftmotor 함수가
	  setDirection 함수로 합쳐졌다.
	4.car 자체에 go_forward go_backward는 없고 엔진의 속력과 방향을 정해주는 engine
	  함수 밖에 없다.
	5.시간 조절도 driver가 결정해 sleep 함수도 부르지 않는다.
'''
import RPi.GPIO as GPIO

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
#set left motor pin to output
GPIO.setup(MOTOR_LEFT_A, GPIO.OUT)
GPIO.setup(MOTOR_LEFT_B, GPIO.OUT)
GPIO.setup(MOTOR_LEFT_PWM, GPIO.OUT)

#set right moto pin to output
GPIO.setup(MOTOR_RIGHT_A, GPIO.OUT)
GPIO.setup(MOTOR_RIGHT_B, GPIO.OUT)
GPIO.setup(MOTOR_RIGHT_PWM, GPIO.OUT)

#create PWM
LeftPwm=GPIO.PWM(MOTOR_LEFT_PWM, 100)
RightPwm=GPIO.PWM(MOTOR_RIGHT_PWM, 100)
	
#public method
#start the car
def startUp():
	LeftPwm.start(0)
	RightPwm.start(0)
	print("Vroom!")

#set engine to move
def engine(leftDirection, rightDirection, leftSpeed, rightSpeed):
	setDirection(leftDirection, rightDirection)
	setSpeed(leftSpeed, rightSpeed)

#turn off the car
def turnOff():
	GPIO.output(MOTOR_LEFT_PWM, GPIO.LOW)
	GPIO.output(MOTOR_RIGHT_PWM, GPIO.LOW)
	LeftPwm.ChangeDutyCycle(0)
	RightPwm.ChangeDutyCycle(0)
	GPIO.cleanup()
	print("turn off")
	


#private method
#set true false value to the motor
def setDirection(leftDirection, rightDirection):
	GPIO.output(MOTOR_LEFT_A, not leftDirection
	GPIO.output(MOTOR_LEFT_B, leftDirection)
	GPIO.output(MOTOR_RIGHT_A, rightDirection)
	GPIO.output(MOTOR_RIGHT_B, not rightDirection)

#change motor speed
def setSpeed(leftSpeed, rightSpeed):
	GPIO.output(MOTOR_LEFT_PWM, GPIO.HIGH)
	GPIO.output(MOTOR_RIGHT_PWM, GPIO.HIGH)
	LeftPwm.ChangeDutyCycle(leftSpeed)
	RightPwm.ChangeDutyCycle(rightSpeed)














