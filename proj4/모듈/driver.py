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
	dummy=1

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
	#li=trackingmodule.navigator()
	#if li[2]==False:
	#when input l
	lSpeed=20
	rSpeed=15
	li=trackingmodule.navigator()
	if direction == 'l' or direction == 'r':
		if li[0]==False:
			lSpeed=0
			rSpeed=20
		elif li[1]==False:
			lSpeed=15
			rSpeed=20
		elif li[2]==False:
			if li[1]==True:
				lSpeed=15
				rSpeed=20
			else:
				lSpeed=20
				rSpeed=15
		elif li[3]==False:
			lSpeed=20
			rSpeed=15
		elif li[4]==False:
			lSpeed=20
			rSpeed=0
		else:
			car.engine(True, True, lSpeed, rSpeed)
			sleep(0.01)
		if direction =='l':
			car.engine(True, True, lSpeed, rSpeed)
		else:
			car.engine(True, True, rSpeed, lSpeed)
		return True	

	else:
		lSpeed=15
		rSpeed=15
		counter=0
		while not li[3]==True:
			li=trackingmodule.navigator()
			car.engine(True, True, 15+counter,0)
			sleep(0.1)
			print(counter)
			if counter<5:
				counter=counter+1
		counter=0
		while not li[4]==True:
			li=trackingmodule.navigator()
			car.engine(True, True, 15+counter, 0)
			sleep(0.1)
			print(counter)
			if counter<10:
				counter=counter+1
		counter=0
		while not li[0]==True:
			li=trackingmodule.navigator()
			car.engine(True, True, 0, 15+counter)
			sleep(0.1)
			print(counter)
			if counter<5:
				counter=counter+1
		counter=0
		while not li[1]==True:
			li=trackingmodule.navigator()
			car.engine(True, True, 0, 15+counter)
			sleep(0.1)
			print(counter)
			if counter<10:
				counter=counter+1
		
		if li[0] and li[1] and li[2] and li[3] and li[4]:
			car.engine(True,True, 15, 15)
			sleep(0.01)	
	#car.engine(True, True, 25, 25)
	#sleep(1)
	'''	
	if not li[1]:
		rspeed=28
	if not li[3]:
		print("rl")
		lspeed=28	
	if not li[0]:
		stop()
		sleep(1)
		lSpeed=0
	if not li[4]:
		stop()
		sleep(1)
		print("rm")
		rSpeed=0;
	'''
	#car.engine(True, True, lSpeed, rSpeed)
	return True

if __name__ == "__main__":
	try:
		Tmode=input("choose 'l or 'r'")
		dis=13###수정해도 됨 
		#차 시동을 건다.
		car.startUp()
		endline= True
		while endline:
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


