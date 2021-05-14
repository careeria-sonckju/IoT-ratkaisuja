from sense_hat import SenseHat

sense = SenseHat()

red = (255, 0, 0)
blue = (0, 0, 255)

while True:
    north = sense.get_compass()
    print("North: %s" % north)


