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
import time

def turn_left():
	dummy=0

def turn_right():
	dummy=0

def U_turn():
	dummy=0

def find_way():
	switch=1
	while switch:
		if False:#need rightT:
			turn_right()
			switch=0
		elif False:#need leftT:
			turn_left()
			switch=0
		elif False:#need U_turn():
			U_turn()
			switch=0
		elif False:#return_to_center():
			gogo_dummy=1
			if trackingModule.bitCount()==5:
				return False
		else:
			return False
			print("?????")
	return True

def lineTracking():
	print("자동주행을 시작합니다.")
	#전진후 좌우 교정과 판단을 동시에
	while keep_going:
		go_forward()
		keep_going=find_way()

	print("자동주행을 마칩니다.")


if __name__ == "__main__":
	try:
		#차 시동을 건다.
		
		car.startUp()
		print("??")
		time.sleep(1)
		car.setDirection(True, True)
		#lineTracking()
		car.setSpeed(30,30)
		print("!!")
		car.setSpeed(30,20)
		time.sleep(1)

		car.setSpeed(20,30)
		time.sleep(1)
		car.setSpeed(30,30)
		time.sleep(1)
	
		time.sleep(1)
		car.setSpeed(0, 0)		
		
		#차 시동을 끈다.
		car.turnOff()
	#ctrl + c 키로 종료한 경우
	except KeyboardInterrupt:
		print("강제종료 하셨습니다.")
	#오류로 인한 종료 시 시동끄기 함수 호출. 없다면 오류로 프로그램이 종료된 이후에도 바퀴가 돌 수 있다.
	finally:
		car.turnOff()


