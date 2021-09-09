from sense_hat import SenseHat
import time
import urllib.request
import threading

ap = SenseHat()

# muuta tähän oman Raspberry-laitteesi id-numero!
deviceid=10

temperatureInterval=2

def commands():
    while True:
        global temperatureInterval
        url = "http://careeriawebappiot.azurewebsites.net/commands/getcommand/"+str(deviceid)
        print(url)
        htmlfile = urllib.request.urlopen(url)
        commandtext = str(htmlfile.read())
        if (commandtext.upper() == "B'TEMPON'"):
            print(commandtext)
            t1.start()
            url = "http://careeriawebappiot.azurewebsites.net/commands/completed/"+str(deviceid)
            urllib.request.urlopen(url)
            print("Komento Temp ON suoritettu.\r")
        elif (commandtext.upper() == "B'TEMPOFF'"):
            print(commandtext)
            #t1.terminate()
            #temperature.terminate()
            url = "http://careeriawebappiot.azurewebsites.net/commands/completed/"+str(deviceid)
            urllib.request.urlopen(url)
            print("Komento Temp OFF suoritettu.\r")
        elif (commandtext.upper() == "B'HUMION'"):
            print(commandtext)
            t2.start()
            url = "http://careeriawebappiot.azurewebsites.net/commands/completed/"+str(deviceid)
            urllib.request.urlopen(url)
            print("Komento Humidity ON suoritettu.\r")
        elif (commandtext.upper() == "B'HUMIOFF'"):
            print(commandtext)
            #t2.terminate
            #humidity.terminate()
            url = "http://careeriawebappiot.azurewebsites.net/commands/completed/"+str(deviceid)
            urllib.request.urlopen(url)
            print("Komento Humidity OFF suoritettu.\r")
        elif (commandtext.upper() == "B'MBARON'"):
            print(commandtext)
            t3.start()
            url = "http://careeriawebappiot.azurewebsites.net/commands/completed/"+str(deviceid)
            urllib.request.urlopen(url)
            print("Komento Pressure ON suoritettu.\r")
        elif (commandtext.upper() == "B'MBAROFF'"):
            print(commandtext)
            #t3.terminate()
            #pressure.terminate()
            url = "http://careeriawebappiot.azurewebsites.net/commands/completed/"+str(deviceid)
            urllib.request.urlopen(url)
            print("Komento Pressure OFF suoritettu.\r")
        else:
            print("Ei ajettavia komentoja, temperatureInterval="+str(temperatureInterval))
            
        time.sleep(3)
        
def temperature():
    global temperatureInterval
    while True:
        type=1
        temp = ap.get_temperature()-12
        print("Temp: %s C" % temp)
        url = "http://careeriawebappiot.azurewebsites.net/measurements/store/"+str(deviceid)+"?value="+str(temp)+"&type="+str(type)
        print(url)
        htmlfile = urllib.request.urlopen(url)
        htmltext = htmlfile.read()
        print("Lämpötila tallennettu: " + str(htmltext))
        time.sleep(temperatureInterval)        

def humidity():
    while True:
        type=2
        humid = ap.get_humidity()
        print("Humidity: %s RH" % humid)
        url = "http://careeriawebappiot.azurewebsites.net/measurements/store/"+str(deviceid)+"?value="+str(humid)+"&type="+str(type)
        print(url)
        htmlfile = urllib.request.urlopen(url)
        htmltext = htmlfile.read()
        print("Kosteus tallennettu: " + str(htmltext))
        time.sleep(2)
        
def pressure():
    while True:
        type=3
        mbars = ap.get_pressure()
        print("Pressure: %s mbar" % mbars)
        url = "http://careeriawebappiot.azurewebsites.net/measurements/store/"+str(deviceid)+"?value="+str(mbars)+"&type="+str(type)
        print(url)
        htmlfile = urllib.request.urlopen(url)
        htmltext = htmlfile.read()
        print("Ilmanpaine tallennettu: " + str(htmltext))
        time.sleep(3)

t0 = threading.Thread(target=commands)
t1 = threading.Thread(target=temperature)
t2 = threading.Thread(target=humidity)
t3 = threading.Thread(target=pressure)

t0.start()
#t1.start()
#t2.start()
#t3.start()