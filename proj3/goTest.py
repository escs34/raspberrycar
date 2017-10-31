import PPicar
import ultraModule
from time import sleep

#there is no need to change the module, just change this interface
def go_forward(speed):
	PPicar.engine(True, True, speed, speed-0.4)

def go_backward(speed):
	PPicar.engine(False, False, speed, speed-4.8)
	
def stop():
	PPicar.engine(True, True, 0, 0)

#left swing turn : only right motor
def left_swing_turn():
	PPicar.engine(True, True, 0, 48)

def right_swing_turn():
	PPicar.engine(True, True, 53, 0)

def left_point_turn(speed):
	PPicar.engine(False, True, speed, speed)

def right_point_turn(speed):#left moter true, right motor false
	PPicar.engine(True, False, speed, speed)

#need infinitive turn

#need print current status

if __name__ == "__main__":
	PPicar.startUp()

	go_forward(50)
	sleep(1)
	go_backward(50)
	sleep(1)
	'''sleep(0.2)
	stop()
	sleep(0.2)
	
	go_forward(50)
	sleep(0.2)
	stop()

	sleep(0.2)

	go_forward(50)
	sleep(0.2)
	stop()
	sleep(0.2)

	go_forward(50)
	sleep(0.2)
	stop()
	sleep(0.2)

	go_forward(50)
	sleep(0.2)
	stop()
	sleep(0.2)'''
	
	
	PPicar.turnOff()
	print('clear')




