from sense_hat import SenseHat
import time
sense = SenseHat()

while True:
    accel_only = sense.get_accelerometer()
    print("p: {pitch}, r: {roll}, y: {yaw}".format(**accel_only))
#     time.sleep(1)