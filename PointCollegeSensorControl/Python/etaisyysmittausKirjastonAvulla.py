from multiprocessing import Process
from Bluetin_Echo import Echo
import time

TRIGGER_PIN = 23
ECHO_PIN = 24

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
def distanceMeasure():
    while True:
        speed_of_sound = 340
        echo = Echo(TRIGGER_PIN, ECHO_PIN, speed_of_sound)

        result = echo.read('cm', 1)
        # Print result.
        print(result, 'cm')

        # Number of distance measurements to average.
        samples = 5
        # Get an average of distance measurements.
        result = echo.read('cm', samples)
        # Print result.
        print(result, 'cm')
        # GPIO cleanup
        echo.stop()

def main():
    p1 = Process(target=distanceMeasure, args=())
    p1.start()
    #p1.join()
    print('pääohjelma päättyi')

if __name__ == '__main__':
    main()

