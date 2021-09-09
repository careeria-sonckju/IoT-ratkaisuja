#!/usr/bin/env python
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
GPIO.setwarnings(False)
reader = SimpleMFRC522()
i=0
try:
    while True:
        i=i+1
        id, text = reader.read()
        print("Kierros="+str(i))
        print(id)
        print(text)
finally:
    GPIO.cleanup()
