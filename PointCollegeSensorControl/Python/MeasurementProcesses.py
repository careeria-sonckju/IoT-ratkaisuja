from multiprocessing import Process
import multiprocessing
#from sense_hat import SenseHat
import urllib.request
import time
#https://pymotw.com/2/multiprocessing/basics.html
#https://stackoverflow.com/questions/11515944/how-to-use-multiprocessing-queue-in-python
#https://betterprogramming.pub/introduction-to-message-queue-with-rabbitmq-python-639e397cb668

#ap = SenseHat()
# muuta tähän oman Raspberry-laitteesi id-numero!
deviceid=9

temperatureInterval=2
humidityInterval=2
pressureInterval=2

def temperature(q1):
    while True:
        global temperatureInterval
        while not q1.empty():
            event = q1.get()
        if (event == "TEMPON"):
            print("Lämpötilamittaus / Queue 1 / on päällä ", event)
            type=1
            #temp = ap.get_temperature()-12
            temp=21
            print("Temp: %s C" % temp)
            url = "http://careeriawebappiot.azurewebsites.net/measurements/store/"+str(deviceid)+"?value="+str(temp)+"&type="+str(type)
            print(url)
            htmlfile = urllib.request.urlopen(url)
            htmltext = htmlfile.read()
            print("Lämpötila tallennettu: " + str(htmltext))
        else:
            print("Lämpötilaa ei mitata tällä hetkellä!")

        time.sleep(temperatureInterval)

def humidity(q2):
    while True:
        while not q2.empty():
            event = q2.get()
        if (event == "HUMION"):
            print("Kosteuden mittaus / Queue 2 / on päällä ", event)
            type=2
            #humid = ap.get_humidity()
            humid=31
            print("Humidity: %s RH" % humid)
            url = "http://careeriawebappiot.azurewebsites.net/measurements/store/"+str(deviceid)+"?value="+str(humid)+"&type="+str(type)
            print(url)
            htmlfile = urllib.request.urlopen(url)
            htmltext = htmlfile.read()
            print("Kosteus tallennettu: " + str(htmltext))
        else:
            print("Kosteutta ei mitata tällä hetkellä!")

        time.sleep(humidityInterval)
    
def pressure(q3):
    while True:
        while not q3.empty():
            event = q3.get()
        if (event == "MBARON"):
            print("Ilmanpaineen mittaus / Queue 3 / on päällä ", event)
            type=3
            #mbars = ap.get_pressure()
            mbars=1001
            print("Pressure: %s mbar" % mbars)
            url = "http://careeriawebappiot.azurewebsites.net/measurements/store/"+str(deviceid)+"?value="+str(mbars)+"&type="+str(type)
            print(url)
            htmlfile = urllib.request.urlopen(url)
            htmltext = htmlfile.read()
            print("Ilmanpaine tallennettu: " + str(htmltext))
        elif (event == "MBAROFF"): 
            print("Ilmanpainetta ei mitata tällä hetkellä!")
        else: 
            print("outo arvo ", event)
            
        time.sleep(pressureInterval)
def main():
    queue1 = multiprocessing.Queue()
    queue2 = multiprocessing.Queue()
    queue3 = multiprocessing.Queue()
    p1 = Process(target=temperature, args=(queue1,))
    #p1.start()
    p2 = Process(target=humidity, args=(queue2,))
    #p2.start()
    p3 = Process(target=pressure, args=(queue3,))
    p3.start()
    queue1.put("initializing")
    queue2.put("initializing")
    queue3.put("initializing")
    while True:
        url = "http://careeriawebappiot.azurewebsites.net/commands/getcommand/"+str(deviceid)
        print(url)
        htmlfile = urllib.request.urlopen(url)
        commandtext = str(htmlfile.read())
        if (commandtext.upper() == "B'TEMPON'"):
            print(commandtext)
            queue1.put("TEMPON")
            #p1.start()
            #p1.join()
            url = "http://careeriawebappiot.azurewebsites.net/commands/completed/"+str(deviceid)
            urllib.request.urlopen(url)
            print("Komento Temp ON suoritettu.\r")
        elif (commandtext.upper() == "B'TEMPOFF'"):
            print(commandtext)
            queue1.put("TEMPOFF")
            url = "http://careeriawebappiot.azurewebsites.net/commands/completed/"+str(deviceid)
            urllib.request.urlopen(url)
            print("Komento Temp OFF suoritettu.\r")
        elif (commandtext.upper() == "B'HUMION'"):
            print(commandtext)
            queue2.put("HUMION")
            #p2.join()
            url = "http://careeriawebappiot.azurewebsites.net/commands/completed/"+str(deviceid)
            urllib.request.urlopen(url)
            print("Komento Humidity ON suoritettu.\r")
        elif (commandtext.upper() == "B'HUMIOFF'"):
            print(commandtext)
            queue2.put("HUMIOFF")
            url = "http://careeriawebappiot.azurewebsites.net/commands/completed/"+str(deviceid)
            urllib.request.urlopen(url)
            print("Komento Humidity OFF suoritettu.\r")
        elif (commandtext.upper() == "B'MBARON'"):
            print(commandtext)
            queue3.put("MBARON")
            #p3.join()
            url = "http://careeriawebappiot.azurewebsites.net/commands/completed/"+str(deviceid)
            urllib.request.urlopen(url)
            print("Komento Pressure ON suoritettu.\r")
        elif (commandtext.upper() == "B'MBAROFF'"):
            print(commandtext)
            queue3.put("MBAROFF")
            url = "http://careeriawebappiot.azurewebsites.net/commands/completed/"+str(deviceid)
            urllib.request.urlopen(url)
            print("Komento Pressure OFF suoritettu.\r")
        else:
            print("Ei ajettavia komentoja, temperatureInterval="+str(temperatureInterval))
        time.sleep(3)

    print('finished main')

if __name__ == '__main__':

    main()