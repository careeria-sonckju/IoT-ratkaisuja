from multiprocessing import Process
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
def distanceMeas():
    while True:
        try:
            GPIO.setmode(GPIO.BCM)
            PIN_TRIGGER = 23 #Sensorin trigger-pinni
            PIN_ECHO = 24 #Sensorin kaiku-pinni

            GPIO.setup(PIN_TRIGGER, GPIO.OUT) #Trigger-pinni on output-tyyppinen
            GPIO.setup(PIN_ECHO, GPIO.IN) #Echo-pinni on input-tyyppinen

            GPIO.output(PIN_TRIGGER, GPIO.LOW) #Trigger-pinni asetetaan pois
            print("Odotetaan sensorin asettumista")
            time.sleep(2)
            print("Mittaa etäisyyttä")
            GPIO.output(PIN_TRIGGER, GPIO.HIGH) #Trigger-pinni asetetaan päälle --> lähettää ääntä
            time.sleep(0.00001) #odotetaan 1 nanosekunti
            GPIO.output(PIN_TRIGGER, GPIO.LOW)  #Trigger-pinni asetetaan pois --> ei lähetä ääntä

            while GPIO.input(PIN_ECHO)==0:
                pulse_start_time = time.time()
            while GPIO.input(PIN_ECHO)==1:
                pulse_end_time = time.time()

            pulse_duration = pulse_end_time - pulse_start_time
            distance = round(pulse_duration * 17150, 2)
            print("Etäisyys on: ",distance,"cm")

        finally:
            GPIO.cleanup()
            
        time.sleep(2)

def main():
    p1 = Process(target=distanceMeas, args=())
    p1.start()
    #p1.join()
    print('pääohjelma päättyi')

if __name__ == '__main__':
    main()

