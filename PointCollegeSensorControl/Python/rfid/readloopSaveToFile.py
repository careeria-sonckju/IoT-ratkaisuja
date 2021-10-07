#!/usr/bin/env python3

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import sys
import os
GPIO.setwarnings(False)
reader = SimpleMFRC522()
def korttienLuku(arg1):
    tiedosto=""
    i=0
    try:
        #jos ei saada argumenttia jostain syystä käytetään vakiotiedostoa cards.txt
        if (arg1 is None):
            filename="cards.txt"
        else:
            filename=arg1
        name = "RFID-kortteja"
        tiedosto = open(filename, "w")
        tiedosto.write(name+"\n")
        while True:
            tiedosto = open(filename, "a")
            i=i+1
            id, text = reader.read()
            tagi=str(id)
            tiedosto.write(tagi+"\n")
            print("Kierros = "+str(i)+"\n")
            print(tagi)
            print(text)
            #seuraavan kortin lukeminen päättää silmukan
            if (id==1055837332172):
                break
    finally:
        tiedosto.close()
        GPIO.cleanup()
def main(arguments):
    if len(arguments) == 1:
        print("main-rutiinista: "+arguments[0])
        korttienLuku(arguments[0])
    else:
        print ("You must supply at least one parameter for the file and path")
if __name__ == "__main__":
    main(sys.argv[1:])