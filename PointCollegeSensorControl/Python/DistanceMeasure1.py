from multiprocessing import Process
import urllib.request
import time
#https://pymotw.com/2/multiprocessing/basics.html
# muuta tähän oman Raspberry-laitteesi id-numero!
deviceid=9

distanceInterval=2

def distanceMeas():
    global distanceInterval
    while True:
        type=98 #etäisyys on tyyppiä 98
        dist = 2 #aluksi kovakoodattu kakkonen
        print("Mitataan etäisyyttä sensorilla")
        url = "http://careeriawebappiot.azurewebsites.net/measurements/store/"+str(deviceid)+"?value="+str(dist)+"&type="+str(type)
        print(url)
        htmlfile = urllib.request.urlopen(url)
        htmltext = htmlfile.read()
        print("Etäisyysmittausarvo on tallennettu: " + str(htmltext))
        time.sleep(distanceInterval)        

def main():
    while True:
        url = "http://careeriawebappiot.azurewebsites.net/commands/getcommand/"+str(deviceid)
        print(url)
        htmlfile = urllib.request.urlopen(url)
        commandtext = str(htmlfile.read())
        if (commandtext.upper() == "B'DISTON'"):
            print(commandtext)
            p1 = Process(target=distanceMeas, args=())
            p1.start()
            #p1.join()
            url = "http://careeriawebappiot.azurewebsites.net/commands/completed/"+str(deviceid)
            urllib.request.urlopen(url)
            print("Komento Dist ON suoritettu.\r")
        elif (commandtext.upper() == "B'DISTOFF'"):
            print(commandtext)
            if (p1.is_alive()):
                p1.terminate()
            url = "http://careeriawebappiot.azurewebsites.net/commands/completed/"+str(deviceid)
            urllib.request.urlopen(url)
            print("Komento Dist OFF suoritettu.\r")
        
        else:
            print("Ei ajettavia komentoja, distanceInterval="+str(distanceInterval))
        
        time.sleep(3)

    print('finished main program')

if __name__ == '__main__':
    main()

