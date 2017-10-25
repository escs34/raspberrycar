import car
from time import sleep

if __name__ == "__main__":
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






