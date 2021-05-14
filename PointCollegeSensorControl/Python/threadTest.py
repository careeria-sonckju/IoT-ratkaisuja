from threading import Thread, Event
import urllib.request
import time
# muuta tähän oman Raspberry-laitteesi id-numero!
deviceid=1

def controlThings(stop0):
    while not stop0.isSet():
        print('readingsomething() running')
        time.sleep(1)
        
        url = "http://careeriawebappiot.azurewebsites.net/commands/getcommand/"+str(deviceid)
        print(url)
        htmlfile = urllib.request.urlopen(url)
        commandtext = str(htmlfile.read())
        if (commandtext.upper() == "B'TEMPON'"):
            print(commandtext)
            url = "http://careeriawebappiot.azurewebsites.net/commands/completed/"+str(deviceid)
            urllib.request.urlopen(url)
            print("Komento Temp ON suoritettu.\r")
            thread2.start()
            thread2.join(2)
        elif (commandtext.upper() == "B'TEMPOFF'"):
            print(commandtext)
            stop2.set()
            url = "http://careeriawebappiot.azurewebsites.net/commands/completed/"+str(deviceid)
            urllib.request.urlopen(url)
            print("Komento Temp ON suoritettu.\r")
        else:
            print("Ei ajettavia komentoja")
        

def readingsomething(stop1):
    while not stop1.isSet():
        print('readingsomething() running')
        time.sleep(1)

def readingsomeotherthing(stop2):
    while not stop2.isSet():
        print('readingsomeotherthing() running')
        time.sleep(2)
        

if __name__ == '__main__':
    stop0 = Event()
    stop1 = Event()
    stop2 = Event()
    thread0 = Thread(target=controlThings, args=(stop0,))
    thread1 = Thread(target=readingsomething, args=(stop1,))
    thread2 = Thread(target=readingsomeotherthing, args=(stop2,))
    thread0.start()
    thread1.start() 
    #thread2.start()


    try:
        thread0.join()
        thread1.join()
        #thread2.join()
    except KeyboardInterrupt:
        print('catched KeyboardInterrupt')
        stop0.set()
        stop1.set()
        stop2.set()
        #save the file

    print('EXIT __main__')