from sense_hat import SenseHat

sense = SenseHat()

red = (255, 0, 0)
blue = (0, 0, 255)
sense = SenseHat()
while True:
    #Get the direction of North in degrees (compared to the USB ports direction)
    #360/0° is North, 90 is East, 270 is West and 180 is South
    #compass only
    #sense.set_imu_config(True, False, False)  # enable only the compass
    direction = sense.get_compass()
    print("direction: %s" % direction)
    if (direction > 0 and direction < 45):
        print("Pohjoinen")
    elif (direction >= 45 and direction < 135):
        print("Itä")
    elif (direction >= 135 and direction < 215):
        print("Etelä")
    elif (direction >= 215 and direction < 305):
        print("Länsi")
    elif (direction >= 305 and direction < 360):
        print("Pohjoinen360")
    else:
        print("suunta tuntematon")
