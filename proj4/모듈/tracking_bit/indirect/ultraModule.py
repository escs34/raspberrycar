######################################################################
#작성일: 11/1
#마지막 변경일: 11/1
#작성자: 20132885 손태선
#기능: 정면의 장애물의 거리를 파악함.
#입력: 없음
#출력: 장애물의 거리
######################################################################


import RPi.GPIO as GPIO # import GPIO librery
import time

GPIO.setmode(GPIO.BOARD)

trig=33
echo=31

#ultrasonic sensor setting
GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)

def getDistance():
    '''return obstacle's distance'''
    GPIO.output(trig,False)
    time.sleep(0.5)
    GPIO.output(trig,True)
    time.sleep(0.00001)
    GPIO.output(trig,False)
    while GPIO.input(echo)==0:
        pulse_start=time.time()
    while GPIO.input(echo)==1:
        pulse_end=time.time()
    pulse_duration=pulse_end-pulse_start
    distance=pulse_duration*17000
    distance=round(distance,2)
    return distance

