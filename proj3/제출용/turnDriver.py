######################################################################
#작성일: 11/1
#마지막 변경일: 11/1
#작성자: 20132885 손태선
#기능: 차를 운전함. 실행파일
#입력: 좌회전 또는 우회전 키보드 입력
#출력: car module로 방향, 속도 출력
######################################################################
'''운전자가 휠을 돌리고 엑셀을 밟는 것 처럼 차에 신호를 보냅니다.
이렇게 car와 driver를 나누면 이후 추가될 다른 요구에도 driver의
행동만 바꾸면 되니 car 모듈을 수정할 필요가 없습니다.
#주의: 수행하려는 장소를 바꿀때마다 코드의 세부수치를 조정해주어야한다.
 바뀐점
1.go_forward, go_backward에 지속 시간 요구조건이 사라짐
2.swing_turn, point_turn이 추가됨
3.장애물을 포착하는 ultraModule이 추가됨
'''

import car
import ultraModule
from time import sleep

#전진
def go_forward(speed):
	PPicar.engine(True, True, speed, speed+0.7)
#후진
def go_backward(speed):
	PPicar.engine(False, False, speed, speed-4.8)
#멈춤	
def stop():
	PPicar.engine(True, True, 0, 0)

#turn은 두 종류 다 5번에 나누어서 회전합니다.
#direction이 True이면 left, False이면 right으로 swing turn
def swing_turn(direction, speed, term):
	PPicar.engine(True, True, speed2 * not direction, speed * direction)
	sleep(term)
	PPicar.engine(True, True, speed2 * not direction, speed * direction)
	sleep(term)
	PPicar.engine(True, True, speed2 * not direction, speed * direction)
	sleep(term)
	PPicar.engine(True, True, speed2 * not direction, speed * direction)
	sleep(term)
	PPicar.engine(True, True, speed2 * not direction, speed * direction)
	sleep(term)

#direction이 True이면 left, False이면 right으로 point turn
def point_turn(direction, speed, term):
	PPicar.engine(not direction, direction, speed, speed)
	sleep(term)
	PPicar.engine(not direction, direction, speed, speed)
	sleep(term)
	PPicar.engine(not direction, direction, speed, speed)
	sleep(term)
	PPicar.engine(not direction, direction, speed, speed)
	sleep(term)
	PPicar.engine(not direction, direction, speed, speed)
	sleep(term)


if __name__ == "__main__":
	try:
		Tmode=input("choose 'l or 'r'")
		direction=True
		if Tmode == 'l':
			direction = True
		elif Tmode =='r':
			direction = False
		else :
			raise Exception("wrong direction")
		dis=13
		obs=1
		#차 시동을 건다.
		car.startUp()
		#장애물 2개 회피, 좌회전시 point turn, swing turn 우회전시 반대
		while obs<3:
			distance = ultraModule.getDistance()
			if distance > dis:
				print(distance)
				go_forward(25)
			else:
				stop()
				sleep(1)
				if obs==1 ^ direction:
					swing_turn(direction, 40, 0.2)
				else:
					point_turn(direction, 27, 0.2)
				obs+=1
				stop()
				sleep(1)
		go_forward(25)
		sleep(2)
		#차 시동을 끈다.
		car.turnOff()
	#ctrl + c 키로 종료한 경우
	except KeyboardInterrupt:
		print("강제종료 하셨습니다.")
	#오류로 인한 종료 시 시동끄기 함수 호출. 없다면 오류로 프로그램이 종료된 이후에도 바퀴가 돌 수 있다.
	finally:
		car.turnOff()


