from gpiozero import LED
from time import sleep
import urllib.request
import json
import RPi.GPIO as GPIO
#GPIO-modulin asetukset
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
#alustukset
deviceid=0
commandtext=""
# haetaan Raspberry-laitteen id-numero device.dat -nimisestä tiedostosta
try:
    df = open("device.dat","r")
    deviceid = df.read()
    if (deviceid != ''):
        print("Löysin laitekoodin tiedostosta")
    else:
        deviceid=1
except :
    print("Laitekooditiedosto device.dat puuttuu, käytän kovakoodattua laiteid:tä")
    deviceid=1

print("Käytän laitekoodia: " + str(deviceid))

while True:

    url = "http://careeriawebappiot.azurewebsites.net/commands/CO2Monitor/"+str(deviceid)
    response = urllib.request.urlopen(url)
    print(response)
    data = json.load(response)
    print(data)
    for uri in data:
        if uri["DeviceId"] == 99:
            commandtext = uri["Command"]
            break
    print(commandtext)
    if (commandtext.upper() == "ON"):
        print("LED " + commandtext)
        GPIO.output(16,GPIO.HIGH) 
        url = "http://careeriawebappiot.azurewebsites.net/commands/completed/"+str(deviceid)
        urllib.request.urlopen(url)
        print("Komento ON suoritettu.\r")
    elif (commandtext.upper() == "OFF"):
        print("LED " + commandtext)
        GPIO.output(16,GPIO.LOW) 
        url = "http://careeriawebappiot.azurewebsites.net/commands/completed/"+str(deviceid)
        urllib.request.urlopen(url)
        print("Komento OFF suoritettu.\r")
    else:
        print("Ei ajettavia komentoja")
    

    sleep(5)


