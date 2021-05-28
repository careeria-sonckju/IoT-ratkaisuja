import RPi.GPIO as GPIO # Import Raspberry Pi GPIO -kirjasto
import time
from gpiozero import PWMLED #mmm. Ledien kirkkautta voi säätää tällä kirjastolla

Gled = PWMLED(17)
Rled = PWMLED(27)

GPIO.setwarnings(False) #Ignoroidaan mahdolliset virheet
GPIO.setmode(GPIO.BOARD) #Ei käytetä BCM-pinnijärjestystä, vaan fyysistä!
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Asettaa pin10:n input pin:ksi ja asettaa alkuarvoksi = "pulled down" eli pois päältä

while True: #ikiluuppi
    if GPIO.input(10) == GPIO.HIGH:
        print("Button was pressed!")
        #GPIO.output(Gled,GPIO.HIGH) #HIGH tarkoittaa, että pinniin kytketään virta --> LEDI palaa
 
    else:
        print("Button was NOT pressed!")
        #GPIO.output(Gled,GPIO.LOW) #LOW tarkoittaa, ettei virtaa kytketä ko. pinniin
        Gled.value = 1
    time.sleep(1)