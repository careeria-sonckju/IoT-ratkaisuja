from sense_hat import SenseHat

sense = SenseHat()

red = (255, 0, 0)
blue = (0, 0, 255)

while True:
    north = sense.get_compass()
    print("North: %s" % north)

    from sense_hat import SenseHat
sense = SenseHat()
#Get the direction of North in degrees (compared to the USB ports direction)
#360/0° is North, 90 is East, 270 is West and 180 is South
direction = sense.get_compass()
print("direction: %s" % direction)
if (direction > 0 && dirction < 45):
    print("Pohjoinen")
elif (direction >= 45 && direction < 135):
    print("Itä")
elif (direction >= 135 && direction < 215):
    print("Etelä")
elif (direction >= 215 && direction < 305):
    print("Länsi")
elif (direction >= 305 && direction < 360):
    print("Pohjoinen360")
else:
    print("suunta tuntematon")
