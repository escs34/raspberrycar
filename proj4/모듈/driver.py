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

예시 코드와의 차이점
1.자동차에서 해결해야 할 일부 기능을 여기서 해결하던 점 수정 (GPIO.setwarnings(false))
2.주행환경이 바뀔때 마다 출력의 세부수치를 바꿔줘야 하기 때문에
자주 수정할 수 있는 여기서 차량의 전후진, 회전을 결정

'''

import car
import trackingmodule
import ultraModule
from time import sleep

def go_forward(speed):
'''전진

	양 모터의 방향을 True, 속도를 speed로 설정해줍니다.
'''
	car.engine(True, True, speed, speed)

def go_backward(speed):
'''후진
	양 모터의 방향을 False, 속도를 speed로 설정해줍니다.
'''
	car.engine(False, False, speed, speed)

def stop():
'''정지

	차를 정지합니다. car.turnOff()를 부르면 아예 GPIO를 clean시키기 때문에 일시정지에 사용합니다.
'''
	car.engine(True, True, 0, 0)

def swing_turn(direction, speed, term):
'''스윙 턴

	direction이 True이면 left, False이면 right으로 swing turn
'''
	car.engine(True, True, speed * not direction, speed * direction)
	sleep(term)

def point_turn(direction, speed, term):
'''포인트 턴

	direction이 True이면 left, False이면 right으로 point turn
'''
	car.engine(not direction, direction, speed, speed)
	sleep(term)
###이 위의 모든 함수는 임시 함수로 필요에 따라 수정하시면 됩니다.
###아마 스윙턴 포인트 턴 하나로 합쳐놔서 좌우 도는 속도가 다를 수 있어요.



def avoid(direction):
'''장애물 회피 comment 입력 필요'''
	dummy=1

def lineTracking(speed):
'''선을 따라 주행 comment 입력 필요'''
	rSpeed=30
	lSpeed=30
	li=[]
	li=trackingmodule.navigator()#가야 할 방향과 속도를 알려줌

	if not li[0] and not li[1] and not li[2] and not li[3] and not li[4]:
		return	True
	elif not li[1]:
		rspeed=33
	elif not li[3]:
		lspeed=33
	elif not li[0]:
		lSpeed=0
	elif not li[4]:
		rSpeed=0;

	car.engine(True, True, lSpeed, rSpeed)
	return False

if __name__ == "__main__":
	try:
		Tmode=input("choose 'l or 'r'")
		dis=13###수정해도 됨 
		#차 시동을 건다.
		car.startUp()
		while endline:
			way = trackingmodule.myPosition()###추적센서
			distance = ultraModule.getDistance()###초음파센서
			if distance <= dis:
				avoid(Tmode)
			else:
				endline = lineTracking(speed)###dummy로 무한루프
				
		#차 시동을 끈다.
		car.turnOff()
	#ctrl + c 키로 종료한 경우
	except KeyboardInterrupt:
		print("강제종료 하셨습니다.")
	#오류로 인한 종료 시 시동끄기 함수 호출. 없다면 오류로 프로그램이 종료된 이후에도 바퀴가 돌 수 있다.
	finally:
		car.turnOff()


