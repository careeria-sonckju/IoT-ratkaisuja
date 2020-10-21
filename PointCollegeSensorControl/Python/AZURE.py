from sense_hat import SenseHat
import time
import urllib.request

ap = SenseHat()

# muuta tähän oman Raspberry-laitteesi id-numero!
deviceid=1


while True:
    
    temp = ap.get_temperature()-12
    print("Temp: %s C" % temp)
    url = "http://careeriawebappiot.azurewebsites.net/measurements/store/"+str(deviceid)+"?temp="+str(temp)
    print(url)
    htmlfile = urllib.request.urlopen(url)
    htmltext = htmlfile.read()
    print("Lämpötila tallennettu: " + str(htmltext))

    url = "http://careeriawebappiot.azurewebsites.net/commands/getcommand/"+str(deviceid)
    print(url)
    htmlfile = urllib.request.urlopen(url)
    commandtext = str(htmlfile.read())
    if (commandtext != "b''"):
        print(commandtext)
        ap.set_rotation(180)
        ap.show_message("%s" % commandtext, scroll_speed=0.12, text_colour=[255, 20, 20])
        url = "http://careeriawebappiot.azurewebsites.net/commands/completed/"+str(deviceid)
        urllib.request.urlopen(url)
        print("Komento suoritettu.\r")
    else: print("Ei ajettavia komentoja")
    
    ap.set_rotation(180)
    ap.show_message("%.1f C" % temp, scroll_speed=0.12, text_colour=[255, 255, 255])
    time.sleep(5)

