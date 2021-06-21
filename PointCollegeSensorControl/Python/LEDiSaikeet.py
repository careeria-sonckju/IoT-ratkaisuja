import RPi.GPIO as GPIO
import time
import threading
Rled = 25
Gled = 24
Yled = 8
MaxRounds=600

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(Rled,GPIO.OUT)
GPIO.setup(Gled,GPIO.OUT)
GPIO.setup(Yled,GPIO.OUT)

def red():
    round=0
    while (round < MaxRounds):
        sRound=str(round)
        print("Punainen LEDi syttyi"+sRound)
        GPIO.output(Rled,GPIO.LOW)
        time.sleep(1)
        print("Punainen LEDi sammui")
        GPIO.output(Rled,GPIO.HIGH)
        time.sleep(2)
        round=round+1
def green():
    round=0
    while (round < MaxRounds):
        print("Vihreä LEDi syttyi")
        GPIO.output(Gled,GPIO.LOW)
        time.sleep(1)
        print("Vihreä LEDi sammui")
        GPIO.output(Gled,GPIO.HIGH)
        time.sleep(1)
        round=round+1

def yellow():
    round=0
    while (round < MaxRounds):
        print("Keltainen LEDi syttyi")
        GPIO.output(Yled,GPIO.LOW)
        time.sleep(1)
        print("Keltainen LEDi sammui")
        GPIO.output(Yled,GPIO.HIGH)
        time.sleep(1)
        round=round+1

t1 = threading.Thread(target=red)
t2 = threading.Thread(target=green)
t3 = threading.Thread(target=yellow)

t1.start()
t2.start()
t3.start()
