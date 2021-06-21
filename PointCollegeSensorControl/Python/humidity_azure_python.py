from sense_hat import SenseHat
import time
import urllib.request
#Muutettu 14.5.2021 JSO
sense = SenseHat()
#Ledien värit
green = (0, 255, 0)
orange = (245, 113, 5)

# muuta tähän oman Raspberry-laitteesi id-numero!
deviceid=8

while True:
    type=2
    humidity = sense.humidity
    humidity_value = 64 * humidity / 100
    
    print("Temp: %s C" % humidity)
    url = "http://careeriawebappiot.azurewebsites.net/measurements/store/"+str(deviceid)+"?value="+str(humidity)+"&type="+str(type)
    print(url)
    htmlfile = urllib.request.urlopen(url)
    htmltext = htmlfile.read()
    print(htmltext)

    sense.set_rotation(180)        

    pixels = [green if i < humidity_value else orange for i in range(64)]

    sense.set_pixels(pixels)
    time.sleep(5)
