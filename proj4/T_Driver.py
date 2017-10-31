from PPicar import *
from time import sleep

def go_forward(speed, A):
	A.engine(True, True, speed, speed)

def go_backward(speed, A):
	A.engine(False, False, speed, speed-3.75)

def stop(A):
	A.engine(True, True, 0, 0)
	
#left swing turn : only right motor
def left_swing_turn(A):
	A.engine(True, True, 0, 48)

def right_swing_turn(A):
	A.engine(True, True, 53, 0)

def left_point_turn(speed, A):
	A.engine(False, True, speed, speed)

def right_point_turn(speed, A):#left moter true, right motor false
	A.engine(True, False, speed, speed)

#need infinitive turn

#need print current status

if __name__ == "__main__":
	PPicar.LeftPwm.start(0)
	RightPwm.start(0)	
	#A=PPicar.PPicar()


	#print(A.getDistance())
	#go_backward(50, A)
	#sleep(1)
	'''go_backward(50, A)
	sleep(0.2)
	go_backward(50, A)
	sleep(0.2)
	go_backward(50, A)
	sleep(0.2)
	go_backward(50, A)
	sleep(0.2)
	go_backward(50, A)#'''
	sleep(0.2)




	#go_forward(60, 3, A)
	#go_backward(60, 3, A)

	#go_forward(80, 3, A)
	#go_backward(80, 3, A)
	#A.stop()#stop()
	print('clear')




