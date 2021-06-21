#!/usr/bin/env python

import RPi.GPIO as GPIO
GPIO.setwarnings(False)
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()
laskuri=0
while True:
    try:
        laskuri = laskuri + 1
        id, text = reader.read()
        print ("Kierros " + str(laskuri) + ": ")
        print(id)
        print(text)
    finally:
        GPIO.cleanup()
