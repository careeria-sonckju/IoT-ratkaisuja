from sense_hat import SenseHat
sense = SenseHat()
accel_only = sense.get_accelerometer()
print("p: {pitch}, r: {roll}, y: {yaw}".format(**accel_only))