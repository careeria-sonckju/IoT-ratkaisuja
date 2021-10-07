#!/usr/bin/env python3

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import sys
import os
GPIO.setwarnings(False)
reader = SimpleMFRC522()
def korttienLuku():
    tiedosto=""
    i=0
    Yled =31
    deviceid=9
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Yled,GPIO.OUT)
    try:
        filename="cards.txt"
        tiedosto = open(filename, "r")
        while True:
            i=i+1 #kasvatetaan korttluvun laskuria, jotta voidaan seurata monesko lukukerta
            id, text = reader.read() #luetaaan RFID-kortin tiedot
            tagi=str(id) #talletetaan tägin sarjanumero tagi-muuttujaan string-tyyppisenä
            print("i = "+str(i)+"\n")
            print("Tägi = " + tagi)
            print("Text = " + text)
            with open(filename) as tiedosto: #tutkitaan silmukassa, onko luettu kortti kelvollisten tiedostossa
                for line in tiedosto:
                    print ("Line = " + line.lstrip()) #tulostetaaan tiedoston kulloinenkin rivin arvo 
                    if (tagi in line): #kortti löytyi tiedostosta --> ovi aukeaa ja silmukka/etsintä päättyy
                        print('Kulkuoikeus tunnistettu --> Ovi aukeaa / ' + str(i))
                        GPIO.output(Yled,GPIO.HIGH)
                        print("Keltainen LEDi syttyi")
                        break #Tiedoston luku silmukassa päättyy, koska kortti löytyi
                    #ellei korttia löytynyt päädytään tähän kohtaan ohjelmassa ja tulostetaan evätty -ilmoitus
                    print('Korttia ei löydy paikallisesta Cards.txt -tiedostosta --> Kulkuoikeus evätty /' + str(i) )
                    GPIO.output(Yled,GPIO.LOW)
                    print("Keltainen LEDi sammui")
                        
    finally:
        tiedosto.close()
        GPIO.cleanup()
def main():
    korttienLuku()

if __name__ == "__main__":
    main()