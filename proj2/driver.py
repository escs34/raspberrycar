import car
import ultraModule
from time import sleep
'''운전자가 휠을 돌리고 엑셀을 밟는 것 처럼 차에 신호를 보냅니다.
이렇게 car와 driver를 나누면 이후 추가될 다른 요구에도 driver의
행동만 바꾸면 되니 car 모듈을 수정할 필요가 없습니다.'''

#전진
def go_forward(speed, term):
	car.engine(True, True, speed, speed-0.4)
	sleep(term)
#후진
def go_backward(speed, term):
	car.engine(False, False, speed, speed-4.8)
	sleep(term)
#멈춤
def stop():
	car.engine(True, True, 0, 0)
#수행과제 40, 60, 80의 속도로 각각 2초 전 후진 하기
if __name__ == "__main__":
	try:
		#차 시동을 건다.
		car.startUp()
	
		go_Forward(40, 2)
		go_Backward(40, 2)

    		go_Forward(60, 2)      
     		go_Backward(60, 2)

     		go_Forward(80, 2)     
      		go_Backward(80, 2)
		stop()

		#차 시동을 끈다.
		car.turnOff()
	#강제종료시 시동끄기 함수 호출. 없다면 오류로 프로그램이 종료된 이후에도 바퀴가 돌 수 있다.
	except KeyboardInterrupt:
		car.turnOff()
		



