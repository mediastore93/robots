#!/usr/bin/env python

import time
import pigpio

pi = pigpio.pi() # Connect to local Pi.
pin = 18

pi.set_servo_pulsewidth(pin, 1000)
time.sleep(0.5)
pi.set_servo_pulsewidth(pin, 2000)
time.sleep(0.5)
#pi.set_servo_pulsewidth(pin, 1500)
time.sleep(0.5)
pi.set_servo_pulsewidth(pin, 1500)
time.sleep(0.5)


# switch servo off
pi.set_servo_pulsewidth(pin, 0);

pi.stop()
