#!/usr/bin/env python3
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import os
GPIO.setwarnings(False)
reader = SimpleMFRC522()
i=0
try:
    name = "RFID-kortteja"
    file = open("cards.txt", "w")
    file.write(name+"\n")

    while True:
        file = open("cards.txt", "a")
        i=i+1
        id, text = reader.read()
        tagi=str(id)
        file.write(tagi+"\n")
        print("Kierros = "+str(i)+"\n")
        print(tagi)
        print(text)
        
finally:
    file.close()
    GPIO.cleanup()
