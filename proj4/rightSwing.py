import PPicar
import ultraModule
from time import sleep

#there is no need to change the module, just change this interface
def go_forward(speed):
	PPicar.engine(True, True, speed, speed)

def go_backward(speed):
	PPicar.engine(False, False, speed, speed-4.8)
	
def stop():
	PPicar.engine(True, True, 0, 0)

#left swing turn : only right motor
def left_swing_turn():
	PPicar.engine(True, True, 0, 48)
	sleep(1)
def right_swing_turn():
	PPicar.engine(True, True, 63, 0)
	sleep(0.3)
	PPicar.engine(True, True, 63, 0)
	sleep(0.3)
	PPicar.engine(True, True, 63, 0)
	sleep(0.3)
	PPicar.engine(True, True, 63, 0)
	sleep(0.3)
	PPicar.engine(True, True, 63, 0)
	sleep(0.3)

def left_point_turn():
	PPicar.engine(False, True, 30, 30)
	sleep(1)
def right_point_turn():#left moter true, right motor false
	PPicar.engine(True, False, 30, 30)
	sleep(0.2)
	PPicar.engine(True, False, 30, 30)
	sleep(0.2)
	PPicar.engine(True, False, 30, 30)
	sleep(0.2)
	PPicar.engine(True, False, 30, 30)
	sleep(0.2)
	PPicar.engine(True, False, 30, 30)
	sleep(0.2)


if __name__ == "__main__":
	dis=25
	obs=1
	PPicar.startUp()
	
	while obs<3:
		distance = ultraModule.getDistance()
		if distance > dis:
			print(distance)
			go_forward(50)
		else:
			stop()
			sleep(1)
			if obs!=1:
				print(distance)
				right_swing_turn()
			else:
				right_point_turn()
			obs+=1
			stop()
			sleep(1)
			break	
	#go_forward(25)
	#sleep(2)
	PPicar.turnOff()
	print('clear')




