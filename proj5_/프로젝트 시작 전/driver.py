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

if __name__ == "__main__":
	try:
		Tmode=input("choose 'l or 'r'")
		dis=15###수정해도 됨 
		#차 시동을 건다.
		car.startUp()
		if Tmode=='l':
			while True:#기능 테스트 과연 car.engine의 구조는 옳은가
				#속도변환
				car.engine(True,True,30,30)
				car.engine(True,True,30,0)
				car.engine(True,True,0,30)
				#방향전환
				car.engine(False,False,30,30)
				car.engine(False,True,30,30)
				car.engine(True,False,30,30)

		elif Tmode=='r':#engine처럼 일일이 변환할 필요 없는 True, False값이나 변화 없는 것까지 변화 하지 않는다면,
			while True:#그냥 차의 속도와 방향을 따로 조절한다면?
				car.setDirection(True, True)
				car.setSpeed(30, 30)
				car.setSpeed(30, 0)
				car.setSpeed(0, 30)

				car.setDirection(False, True)
				car.setSpeed(30, 0)
				car.setSpeed(30, 0)				
		else:
			while True:#car.setSpeed2
				GPI
				car.engine(True,True,30,0)
				car.engine(True,True,0,30)
				car.engine(False,False,30,30)
				car.engine(False,True,30,30)
				car.engine(True,False,30,30)

		#차 시동을 끈다.
		car.turnOff()
	#ctrl + c 키로 종료한 경우
	except KeyboardInterrupt:
		print("강제종료 하셨습니다.")
	#오류로 인한 종료 시 시동끄기 함수 호출. 없다면 오류로 프로그램이 종료된 이후에도 바퀴가 돌 수 있다.
	finally:
		car.turnOff()


