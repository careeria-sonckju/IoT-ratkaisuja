from sense_hat import SenseHat
import time
import urllib.request

sense = SenseHat()

# muuta tähän oman Raspberry-laitteesi id-numero!
deviceid=8

while True:
    type=1
    temp = sense.get_temperature()-12
    print("Temp: %s C" % temp)
    url = "http://careeriawebsensepiot.azurewebsites.net/measurements/store/"+str(deviceid)+"?value="+str(temp)+"&type="+str(type)
    print(url)
    htmlfile = urllib.request.urlopen(url)
    htmltext = htmlfile.read()
    print(htmltext)

    sense.set_rotation(180)        

    sense.show_message("%.1f C" % temp, scroll_speed=0.12, text_colour=[255, 255, 255])
    time.sleep(5)
