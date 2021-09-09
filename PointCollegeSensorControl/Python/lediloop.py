import RPi.GPIO as GPIO
import time
import threading
Gled = 17 #vihreän ledin pinni on 24
MaxRounds=600

GPIO.setmode(GPIO.BCM) #mitä pin-merkintäjärjestelmää käytetään BCM taikka BOARD https://raspberrypi.stackexchange.com/questions/12966/what-is-the-difference-between-board-and-bcm-for-gpio-pin-numbering
GPIO.setwarnings(False) #poistaa "turhat" varoitukset käytöstä https://www.raspberrypi.org/forums/viewtopic.php?t=252579
GPIO.setup(Gled,GPIO.OUT) #määrittää halutun portin/pinnin output -tyyppiseksi (vrt. IN)

def green():
    round=0
    while (round < MaxRounds):
        print("Vihreä LEDi syttyi")
        GPIO.output(Gled,GPIO.LOW) #LOW tarkoittaa, ettei virtaa kytketä ko. pinniin
        time.sleep(1)
        print("Vihreä LEDi sammui")
        GPIO.output(Gled,GPIO.HIGH) #HIGH tarkoittaa, että pinniin kytketään virta --> LEDI palaa
        time.sleep(1)
        round=round+1

t1 = threading.Thread(target=green)
t1.start()