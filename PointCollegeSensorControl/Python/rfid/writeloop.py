#!/usr/bin/env python3

import RPi.GPIO as GPIO
GPIO.setwarnings(False)
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()
text = input('Type new data to be stored in RFID-memory:')
laskuri=0
while True:
    try:
        laskuri = laskuri + 1
        print("Now place your tag " + str(laskuri) + " to write")
        reader.write(text+str(laskuri))
        print("Written")
    finally:
        GPIO.cleanup()
