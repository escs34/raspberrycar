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
import lightTrack
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
	car.engine(True, True, speed * (not direction), speed * direction)
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
	return 0
	#sample code, 아마 도착시 대각선으로 닿아 있는 편이 좋을 듯
	turn_way=True
	if direction == 'r':
		turn_way=False
	swing_turn(turn_way, 40, 3)
	go_forward(20)
	sleep(1)
	swing_turn(not turn_way, 20, 3)
	go_forward(20)
	sleep(1)
	swing_turn(not turn_way, 20, 3)
	go_forward(20)
	sleep(1)
	#여기까지 했는데 검은 선에 안닿았다. 이 경우 추가 코드 작성도 좋을듯
	#li=trackingmodule.navigator()
	#if 

def lineTracking(direction):
	'''선을 따라 주행 comment 입력 필요

	r은 내부 l는 외부주행
	내부 주행 외부 주행은 서로 요구하는 led방향이 반대
	reverse 여부는 바퀴 출력 순서 반대
	평가 요구사함
	바깥은 좌회전으로
	내부는 우회전으로
	즉 서로 led와 바퀴 출력 순서가 반대

	둘다 안들어온다면 지그재그 주행
	'''
	#일단 바깥주행먼저, 알고리즘을 수정해서 커브 bit, correct bit, 나머지는
	#간단히 2번 3번 비트는  무시한다. 

	lSpeed=30
	rSpeed=30
	bit=not lightTrack.navigator()
	
	if bit & 1  ==True:
		#print("?")
		car.engine(False, True, lSpeed, rSpeed)
		#sleep(0.3)
		#while lightTrack.navigator()>1:
		#	pass
		#print("??")
		#stop()
		#sleep(0.1)
	elif 1<bit<=6:
		#right motor faster22
		car.engine(True, True, lSpeed, rSpeed+5)
		#sleep(0.5)
	elif 6<bit<=24:
		car.engine(True, True, lSpeed+5, rSpeed)
		#sleep(0.5)
	else:
		car.engine(True, True, lSpeed, rSpeed)
		#sleep(1)
	'''if bit & 1 == False:
		car.engine(True, True, 0, rSpeed)
	elif bit>>1 & 1 ==False:
		car.engine(True, True, lSpeed, rSpeed)
	elif bit>>2 & 1 ==False:
		if bit>>3 & 1:
			car.engine(True, True, lSpeed, rSpeed)
		else:
			car.engine(True, True, rSpeed, lSpeed)
	elif bit>>3 & 1==False or bit>>4 & 1 ==False:
		car.engine(True, True, rSpeed, lSpeed)'''

	return True	


if __name__ == "__main__":
	try:
		Tmode=input("choose 'l or 'r'")
		dis=13###수정해도 됨 
		#차 시동을 건다.
		car.startUp()
		endline= True
		#car.engine(True, True, 30, 30)
		#sleep(0.1)
		lSpeed=30
		rSpeed=35
		while endline:
			car.engine(True, True, lSpeed, rSpeed)
			while changed:
				distance = ultraModule.getDistance()###초음파센서
				if distance <= dis:
					avoid(Tmode)
				else:
					endline = lineTracking(Tmode)###dummy로 무한루프
				
		#차 시동을 끈다.
		car.turnOff()
	#ctrl + c 키로 종료한 경우
	except KeyboardInterrupt:
		print("강제종료 하셨습니다.")
	#오류로 인한 종료 시 시동끄기 함수 호출. 없다면 오류로 프로그램이 종료된 이후에도 바퀴가 돌 수 있다.
	finally:
		car.turnOff()


