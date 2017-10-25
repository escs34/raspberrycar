import PPicar
from time import sleep

def go_forward(speed, duration, A):
	A.go(True, True, speed, speed, duration)
	sleep(1)

def go_backward(speed, duration, A):
	A.go(False, False, speed, speed, duration)
	sleep(1)

def left_swing_turn(speed, duration, A):#left swing turn : only right motor
	A.go(True, True, 0, speed, duration)
	sleep(1)

def right_swing_turn(speed, duration, A):
	A.go(True, True, speed, 0, duration)
	sleep(1)

def left_point_turn(speed, duration_time, A):
	A.go(False, True, speed, speed, duration_time)
	sleep(1)
def right_point_turn(speed, duration_time, A):#left moter true, right motor false
	A.go(True, False, speed, speed, duration_time)
	sleep(1)
#need infinitive turn

#need print current status

if __name__ == "__main__":
	A=PPicar.PPicar()
	go_forward(40, 3, A)
	#go_backward(40, 3, A)

	#go_forward(60, 3, A)
	#go_backward(60, 3, A)

	#go_forward(80, 3, A)
	#go_backward(80, 3, A)
	go_forward(0, 1, A)#stop()
	print('clear')




