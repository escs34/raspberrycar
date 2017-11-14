import PPicar
import ultraModule
from time import sleep

#there is no need to change the module, just change this interface
def go_forward(speed):
	PPicar.engine(True, True, speed, speed+0.7)

def go_backward(speed):
	PPicar.engine(False, False, speed, speed-4.8)
	
def stop():
	PPicar.engine(True, True, 0, 0)

#left swing turn : only right motor
#fuse to swing_turn(d, s, t), point_turn(d, s, t)
def left_swing_turn(speed2, term):
	PPicar.engine(True, True, 0, speed2)
	sleep(term)
	PPicar.engine(True, True, 0, speed2)
	sleep(term)
	PPicar.engine(True, True, 0, speed2)
	sleep(term)
	PPicar.engine(True, True, 0, speed2)
	sleep(term)
	PPicar.engine(True, True, 0, speed2)
	sleep(term)

def right_swing_turn(speed, term):
	PPicar.engine(True, True, speed, 0)
	sleep(term)
	PPicar.engine(True, True, speed, 0)
	sleep(term)
	PPicar.engine(True, True, speed, 0)
	sleep(term)
	PPicar.engine(True, True, speed, 0)
	sleep(term)
	PPicar.engine(True, True, speed, 0)
	sleep(term)

def left_point_turn(speed, term):
	PPicar.engine(False, True, speed, speed)
	sleep(term)
	PPicar.engine(False, True, speed, speed)
	sleep(term)
	PPicar.engine(False, True, speed, speed)
	sleep(term)
	PPicar.engine(False, True, speed, speed)
	sleep(term)
	PPicar.engine(False, True, speed, speed)
	sleep(term)

def right_point_turn(speed, term):#left moter true, right motor false
	PPicar.engine(True, False, speed, speed)
	sleep(term)
	PPicar.engine(True, False, speed, speed)
	sleep(term)
	PPicar.engine(True, False, speed, speed)
	sleep(term)
	PPicar.engine(True, False, speed, speed)
	sleep(term)
	PPicar.engine(True, False, speed, speed)
	sleep(term)

if __name__ == "__main__":
	dis=13
	obs=1
	PPicar.startUp()
	Tmode=int(input())
	if Tmode==1:#go to right
		while obs<3:
			distance = ultraModule.getDistance()
			if distance > dis:
				print(distance)
				go_forward(25)
			else:
				stop()
				sleep(1)
				if obs==1:
					right_swing_turn(40, 0.2)
				else:
					right_point_turn(27, 0.2)
				obs+=1
				stop()
				sleep(1)
					
	else:#rewrite when upload
		while obs<3:
			distance = ultraModule.getDistance()
			if distance > dis:
				go_forward(25)
			else:
				stop()
				sleep(1)
				if obs==1:
					left_point_turn(30, 0.2)
				else:
					left_swing_turn(42, 0.2)
				obs+=1
				stop()
				sleep(1)

	go_forward(25)
	sleep(2)
	PPicar.turnOff()
	print('clear')




