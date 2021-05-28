import RPi.GPIO as GPIO # Import Raspberry Pi GPIO -kirjasto

GPIO.setwarnings(False) #Ignoroidaan mahdolliset virheet
GPIO.setmode(GPIO.BOARD) #Ei käytetä BCM-pinnijärjestystä, vaan fyysistä!
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Asettaa pin10:n input pin:ksi ja asettaa alkuarvoksi = "pulled down" eli pois päältä

while True: #ikiluuppi
    if GPIO.input(10) == GPIO.HIGH:
        print("Button was pressed!")