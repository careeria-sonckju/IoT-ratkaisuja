#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()
lkm = 0
Yled =31
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(Yled,GPIO.OUT)
while True:    
    try:
        lkm=lkm+1
        print('Please read the tag: ' + str(lkm))
        id, text = reader.read()
        print(id)
        print(text)
        if ((text[:7])=='Granted'):
            print('Kulkuoikeus ok /' + str(lkm) )
            GPIO.output(Yled,GPIO.HIGH)
            print("Keltainen LEDi syttyi")
        else:
            print('Ei oikeutta / ' + str(lkm))
            GPIO.output(Yled,GPIO.LOW)
            print("Keltainen LEDi sammui")
    finally:
        print("Environment cleaned")
        #GPIO.cleanup()