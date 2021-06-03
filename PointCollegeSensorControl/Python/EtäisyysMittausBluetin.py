from multiprocessing import Process
from Bluetin_Echo import Echo
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM) #Käytetään BCM-mäppäystä pinnien hallintaan
TRIGGER_PIN = 23 #Liipasimen BCM-pinni on 23
ECHO_PIN = 24 #Äänen kaiun BCM-pinni on 24
GPIO.setwarnings(False)
def distanceMeasure():
    while True:
        speed_of_sound = 340
        echo = Echo(TRIGGER_PIN, ECHO_PIN, speed_of_sound) #Echo-mittauksen asetus
        samples = 5 #Montako mittausta otetaan keskiarvolaskentaan
        result = echo.read('cm', samples) # Hae etäisyysmittausten keskiarvo cm:einä
        print(result, 'cm') # Tuloksen tulostaminen
        # GPIO cleanup
        echo.stop()

def main():
    p1 = Process(target=distanceMeasure, args=())
    p1.start()
    #p1.join()
    print('pääohjelma suoritettu')

if __name__ == '__main__':
    main()
