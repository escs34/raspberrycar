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
import trackingModule
import ultraModule
from time import sleep

def stop():
	'''정지

	차를 정지합니다. car.turnOff()를 부르면 아예 GPIO를 clean시키기 때문에 일시정지에 사용합니다.
	'''
	car.engine(True, True, 0, 0)

def swing_turn(direction, speed):
	'''스윙 턴

	direction이 True이면 left, False이면 right으로 swing turn
	'''
	car.engine(True, True, speed * (not direction), speed * direction)

def point_turn(direction, speed):
	'''포인트 턴

	direction이 True이면 left, False이면 right으로 point turn
	'''
	car.engine(not direction, direction, speed, speed)



def avoid(direction):
	'''장애물 회피 comment 입력 필요'''
	#dummy code
	stop()
	sleep(1)
	#return 0
	#sample code, 아마 도착시 대각선으로 닿아 있는 편이 좋을 듯
	if direction == 'l':
		stop()
		sleep(0.1)


		#회전
		car.engine(True, False, 0, 30)
		sleep(1)
		car.engine(False, False, 10, 50)#휘어서 후진? 그냥 후진?
		while not trackingModule.bitCount()>=3:
			pass
		stop()
		sleep(1)		
		car.engine(False, False, 0, 30)
		while ultraModule.getDistance()<30:
			pass
		sleep(0.5)#쪼끔만 더 돌자
		stop()
		sleep(0.1)

		#전진
		car.engine(True, True, 20, 60) 
		#sleep(1)
		while not trackingModule.bit16():
			pass
		stop()
		sleep(1)



def lineTracking(speed):
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

	bit= trackingModule.navigator()
	print(bit)

	if bit==0 or bit==1 or bit ==3 or bit==24 or bit ==16:
		stop()
		sleep(0.1)
		whereToBack=True
		if trackingModule.getBeforeBit()>6:
			whereToBack=False


		#trackingModule.navigator()

		
		point_turn(whereToBack, speed)
		print(whereToBack)
		counter=0

		#trackingModule.navigator()


		while not trackingModule.bit4():
			counter+=1
			print(counter)
			if counter%1500==0:
				point_turn(whereToBack, speed)
			elif counter>60000:
				car.engine(True, True, speed, speed)
				counter=0
		stop()
		sleep(0.1)
		
		car.engine(True, True, speed, speed)
	#trackingModule.navigator()
	return True
	


if __name__ == "__main__":
	try:
		Tmode=input("choose 'l or 'r'")
		dis=16###수정해도 됨 
		#차 시동을 건다.
		car.startUp()
		endline= True
		if Tmode =='l':
			car.engine(True, True, 30, 35)
		else:
			car.engine(True, True, 35, 30)
		sleep(0.1)

		while endline:
			distance = ultraModule.getDistance()###초음파센서
			print("current distance: ", distance)
			if 4< distance < dis:
				print(distance)
				#avoid(Tmode)
			else:
				endline = lineTracking(30)
				
		#차 시동을 끈다.
		car.turnOff()
	#ctrl + c 키로 종료한 경우
	except KeyboardInterrupt:
		print("강제종료 하셨습니다.")
	#오류로 인한 종료 시 시동끄기 함수 호출. 없다면 오류로 프로그램이 종료된 이후에도 바퀴가 돌 수 있다.
	finally:
		car.turnOff()


