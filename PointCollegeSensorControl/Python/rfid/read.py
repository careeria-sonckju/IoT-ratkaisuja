#!/usr/bin/env python3

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
GPIO.setwarnings(False)
reader = SimpleMFRC522()
try:
        id, text = reader.read()
        print(id)
        print(text)
finally:
        GPIO.cleanup()
