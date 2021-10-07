#!/usr/bin/env python3
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
GPIO.setwarnings(False)
reader = SimpleMFRC522()
i=0
try:
    while True:
        i=i+1
        id, text = reader.read()
        tagi=str(id)
        print("Kierros = "+str(i))
        print(tagi)
        print(text)

finally:
    file.close()
    GPIO.cleanup()