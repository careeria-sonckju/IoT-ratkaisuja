from gpiozero import LED
from time import sleep
import urllib.request
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
# muuta tähän oman Raspberry-laitteesi id-numero!
deviceid=1

while True:
    url = "http://careeriawebappiot.azurewebsites.net/commands/getcommand/"+str(deviceid)
    print(url)
    htmlfile = urllib.request.urlopen(url)
    commandtext = str(htmlfile.read())
    if (commandtext == "b'on'"):
        print("LED " + commandtext)
        GPIO.output(16,GPIO.HIGH) 
        url = "http://careeriawebappiot.azurewebsites.net/commands/completed/"+str(deviceid)
        urllib.request.urlopen(url)
        print("Komento ON suoritettu.\r")
    elif (commandtext == "b'off'"):
        print("LED " + commandtext)
        GPIO.output(16,GPIO.LOW) 
        url = "http://careeriawebappiot.azurewebsites.net/commands/completed/"+str(deviceid)
        urllib.request.urlopen(url)
        print("Komento OFF suoritettu.\r")
    else:
        print("Ei ajettavia komentoja")
    
    print("LED2 on")
    GPIO.output(20,GPIO.HIGH)   #taikka suoraan gpiozero-komento: led.on()
    sleep(1)
    GPIO.output(20,GPIO.LOW)  #taikka suoraan gpiozero-komento: led.off()
    print("LEDs off")
    sleep(5)


