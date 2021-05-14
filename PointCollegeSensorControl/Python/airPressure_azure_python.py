from sense_hat import SenseHat
import time
import urllib.request
#Muutettu 14.5.2021 JSO
sense = SenseHat()
#Ledien värit
lily = (147, 41, 217)
orange = (245, 113, 5)

# muuta tähän oman Raspberry-laitteesi id-numero!
deviceid=8

while True:
    type=3
    mbars = sense.get_pressure()
    print("Pressure: %s mbar" % mbars)
    url = "http://careeriawebappiot.azurewebsites.net/measurements/store/"+str(deviceid)+"?value="+str(mbars)+"&type="+str(type)
    print(url)
    htmlfile = urllib.request.urlopen(url)
    htmltext = htmlfile.read()
    print(htmltext)

    sense.set_rotation(180)        
    pressure_value = 64 * mbars / 10000
    pixels = [lily if i < pressure_value else orange for i in range(64)]

    sense.set_pixels(pixels)
    time.sleep(5)
