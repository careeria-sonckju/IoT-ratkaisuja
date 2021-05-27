from gpiozero import LED
from time import sleep
import urllib.request
import RPi.GPIO as GPIO
#GPIO-modulin asetukset
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
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
    url = "http://careeriawebappiot.azurewebsites.net/commands/getcommand/"+str(deviceid)
    print(url)
    htmlfile = urllib.request.urlopen(url)
    commandtext = str(htmlfile.read())
    if (commandtext.upper() == "B'LEDION'"):
        print("LED " + commandtext)
        GPIO.output(17,GPIO.HIGH) 
        url = "http://careeriawebappiot.azurewebsites.net/commands/completed/"+str(deviceid)
        urllib.request.urlopen(url)
        print("Komento LEDION suoritettu.\r")
    elif (commandtext.upper() == "B'LEDIOFF'"):
        print("LED " + commandtext)
        GPIO.output(17,GPIO.LOW) 
        url = "http://careeriawebappiot.azurewebsites.net/commands/completed/"+str(deviceid)
        urllib.request.urlopen(url)
        print("Komento LEDIOFF suoritettu.\r")
    else:
        print("Ei ajettavia komentoja")
    
    sleep(1)


