from multiprocessing import Process
import urllib.request
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#https://pymotw.com/2/multiprocessing/basics.html
# muuta tähän oman Raspberry-laitteesi id-numero!
deviceid=9

distanceLoopInterval=2
sleeptime = 0.8
#Sensorin ohjaus ja luenta-pinnit
trigger_pin = 23
echo_pin = 24



def distanceMeas():
    global distanceLoopInterval
    while True:
        #Asetetaan GPIO:t
        GPIO.setup(trigger_pin, GPIO.OUT)
        GPIO.setup(echo_pin, GPIO.IN)
        GPIO.output(trigger_pin, False)
        type=98 #etäisyysmittauksen tyyppi Azure-tietokannassa on 98
        Etaisyys = 2 #Etaisyys aluksi kovakoodattu kakkonen
        print("Mitataan etäisyyttä sensorilla")
        GPIO.output(trigger_pin, True) #etäisyysmittaus 10us pitkällä trigger signaalilla
        time.sleep(0.00001)
        GPIO.output(trigger_pin, False)

        KaynnistysAika = time.time()
        while GPIO.input(echo_pin) == 0:
            KaynnistysAika = time.time()

        while GPIO.input(echo_pin) == 1:
            SammutusAika = time.time()
        Kesto = SammutusAika - KaynnistysAika
        Etaisyys = (Kesto * 34300) / 2  #etäisyyden laskenta (äänennopeus 34300 cm/s --> jaetaan kahdella, koska ääni menee edestakaisin
        if Etaisyys < 2 or (round(Etaisyys) > 400): #Tarkistetaan, että tulos on mittausalueella
            print("Mittausalueen ulkopuolella") # Virhe, jos tulos mittausalueen ulkopuolella
            print("------------------------------")
        else: #muuten muotoillaan tulos
            Etaisyys = format((Kesto * 34300) / 2, '.2f')
            print("Etäisyys on ", Etaisyys," cm")
            print("------------------------------")
        # break between measurement
        time.sleep(sleeptime)
        
        url = "http://careeriawebappiot.azurewebsites.net/measurements/store/"+str(deviceid)+"?value="+str(Etaisyys)+"&type="+str(type)
        print(url)
        htmlfile = urllib.request.urlopen(url)
        htmltext = htmlfile.read()
        print("Etäisyysmittausarvo on tallennettu: " + str(htmltext))
        time.sleep(distanceLoopInterval)        

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
            print("Ei ajettavia komentoja, distanceLoopInterval="+str(distanceLoopInterval))
        
        time.sleep(3)

    print('finished main program')

if __name__ == '__main__':
    main()

