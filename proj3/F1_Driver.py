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

def left_swing_turn(speed, duration_time, A):#left swing turn 이 오른바퀴만 움직이는 것
	A.go(True, True, 0, speed, duration_time)
	sleep(1)

def right_swing_turn(speed, duration_time, A):
	A.go(True, True, speed, 0, duration_time)
	sleep(1)

def left_point_turn(speed, duration_time, A):
	A.go(False, True, speed, speed, duration_time)
	sleep(1)
def right_point_turn(speed, duration_time, A):#왼쪽모터 전진, 오른쪽 모터 후진
	A.go(True, False, speed, speed, duration_time)
	sleep(1)
#무한히 돌면서 장애물 발생시 이동 같은 메소드 필요

#현재 속도나 방향 같은거 출력해주는 메소드 필요


