import PPicar
from time import sleep

if __name__ == "__main__":
	A=PPicar.PPicar()
	go_forward(40, 3, A)
	go_backward(40, 3, A)

	go_forward(60, 3, A)
	go_backward(60, 3, A)

	go_forward(80, 3, A)
	go_backward(80, 3, A)

	print('clear')

def go_forward(speed, duration_time, A):
	A.go(True, True, speed, speed, duration_time)
	sleep(1)

def go_backward(speed, duration_time, A):
	A.go(False, False, speed, speed, duration_time)
	sleep(1)

def left_swing_turn(speed, duration_time, A):#left swing turn : only right motor
	A.go(True, True, 0, speed, duration_time)
	sleep(1)

def right_swing_turn(speed, duration_time, A):
	A.go(True, True, speed, 0, duration_time)
	sleep(1)

def left_point_turn(speed, duration_time, A):
	A.go(False, True, speed, speed, duration_time)
	sleep(1)
def right_point_turn(speed, duration_time, A):#left moter true, right motor false
	A.go(True, False, speed, speed, duration_time)
	sleep(1)
#need infinitive turn

#need print current status


