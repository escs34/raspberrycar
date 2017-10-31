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
	sleep(1)
def right_swing_turn():
	PPicar.engine(True, True, 53, 0)

def left_point_turn():
	PPicar.engine(False, True, 40, 40)
	sleep(1)
def right_point_turn(speed):#left moter true, right motor false
	PPicar.engine(True, False, 40, 40)

#need infinitive turn

#need print current status

if __name__ == "__main__":
	dis=25
	obs=1
	PPicar.startUp()
	
	while obs<3:
		distance = ultraModule.getDistance()
		if distance > dis:
			go_forward(50)
		else:
			stop()
			if obs==1:
				left_point_turn()
			else:
				left_swing_turn()
			obs+=1
			stop()
			sleep(1)
			break
	#go_forward(25)
	#sleep(2)	
	PPicar.turnOff()
	print('clear')




