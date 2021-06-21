#import RPi.GPIO as GPIO # Import Raspberry Pi GPIO -kirjasto
import time
from gpiozero import PWMLED, Button  #mmm. Ledien kirkkautta voi säätää tällä PWMLED kirjastolla

Gled = PWMLED(17) #tämä siis GPIO17
Rled = PWMLED(27)

button = Button(2) #tämä siis GPIO2

while True:
    time.sleep(1)
    if button.is_pressed:
        print("Pressed")
        Gled.value = 1  #täydellä valoteholla
    else:
        print("Released")
        Gled.value = 0.25  #neljännes valoteholla
    time.sleep(1)
    Gled.value = 0  #kokonaan pois