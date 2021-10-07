#!/usr/bin/env python3

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import urllib.request
import json

while True:
    reader = SimpleMFRC522()
    lkm = 0
    Yled =31
    deviceid=9
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Yled,GPIO.OUT)
    try:
        lkm=lkm+1
        print('Lue ensimmäinen tagi: ' + str(lkm))
        id, text = reader.read()
        print(id)
        print(text)
        url = "http://raspberrryiotserver.azurewebsites.net/RFIDTags/GetRFIDTag/?Tag="+str(id)
        print(url)
        htmlfile = urllib.request.urlopen(url)
        textResponse = str(htmlfile.read())
        print(textResponse)
        if ((textResponse)=="b'0'"):
            print('Korttia ei löydy Azure-palvelusta --> Kulkuoikeus evätty /' + str(lkm) )
            GPIO.output(Yled,GPIO.LOW)
            print("Keltainen LEDi sammui")
        else:
            print('Kulkuoikeus tunnistettu --> Ovi aukeaa / ' + str(lkm))
            GPIO.output(Yled,GPIO.HIGH)
            print("Keltainen LEDi syttyi")
    finally:
        print("Environment cleaned")
        GPIO.cleanup()
