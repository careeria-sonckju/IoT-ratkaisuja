from sense_hat import SenseHat

sense = SenseHat()

green = (0, 255, 0)
white = (255, 255, 255)

while True:
    pressure = sense.get_pressure()
    pressure_value = 64 * pressure / 10000
    print(pressure)

    pixels = [green if i < pressure_value else white for i in range(64)]

    sense.set_pixels(pixels)