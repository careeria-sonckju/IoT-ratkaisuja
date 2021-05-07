from multiprocessing import Process
from sense_hat import SenseHat
import urllib.request
import time
#https://pymotw.com/2/multiprocessing/basics.html
ap = SenseHat()
# muuta tähän oman Raspberry-laitteesi id-numero!
deviceid=9

temperatureInterval=2

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
def main():
    p1 = Process(target=temperature, args=())
    p1.start()
    p2 = Process(target=humidity, args=())
    p2.start()
    p3 = Process(target=pressure, args=())
    p3.start()
    while True:
        url = "http://careeriawebappiot.azurewebsites.net/commands/getcommand/"+str(deviceid)
        print(url)
        htmlfile = urllib.request.urlopen(url)
        commandtext = str(htmlfile.read())
        if (commandtext.upper() == "B'TEMPON'"):
            print(commandtext)
            if (not p1.is_alive()):
                p1.start()
            #p1.join()
            url = "http://careeriawebappiot.azurewebsites.net/commands/completed/"+str(deviceid)
            urllib.request.urlopen(url)
            print("Komento Temp ON suoritettu.\r")
        elif (commandtext.upper() == "B'TEMPOFF'"):
            print(commandtext)
            if (p1.is_alive()):
                p1.terminate()
            url = "http://careeriawebappiot.azurewebsites.net/commands/completed/"+str(deviceid)
            urllib.request.urlopen(url)
            print("Komento Temp OFF suoritettu.\r")
        elif (commandtext.upper() == "B'HUMION'"):
            print(commandtext)
            if (not p2.is_alive()):
                p2.start()
            #p2.join()
            url = "http://careeriawebappiot.azurewebsites.net/commands/completed/"+str(deviceid)
            urllib.request.urlopen(url)
            print("Komento Humidity ON suoritettu.\r")
        elif (commandtext.upper() == "B'HUMIOFF'"):
            print(commandtext)
            if (p2.is_alive()):
                p2.terminate()
            url = "http://careeriawebappiot.azurewebsites.net/commands/completed/"+str(deviceid)
            urllib.request.urlopen(url)
            print("Komento Humidity OFF suoritettu.\r")
        elif (commandtext.upper() == "B'MBARON'"):
            print(commandtext)
            if (not p3.is_alive()):
                p3.start()
            #p3.join()
            url = "http://careeriawebappiot.azurewebsites.net/commands/completed/"+str(deviceid)
            urllib.request.urlopen(url)
            print("Komento Pressure ON suoritettu.\r")
        elif (commandtext.upper() == "B'MBAROFF'"):
            print(commandtext)
            if (not p3.is_alive()):
                p3.terminate()
            url = "http://careeriawebappiot.azurewebsites.net/commands/completed/"+str(deviceid)
            urllib.request.urlopen(url)
            print("Komento Pressure OFF suoritettu.\r")
        else:
            print("Ei ajettavia komentoja, temperatureInterval="+str(temperatureInterval))
        time.sleep(3)

    print('finished main')

if __name__ == '__main__':

    main()
