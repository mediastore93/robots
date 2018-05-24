from gpiozero import Robot
import time

robby = Robot(left = (7, 8), right = (9, 10))

def forward():
    robby.forward()
def backward():
    robby.backward()
def left():
    robby.left()
def right():
    robby.right()
def stop():
    robby.stop()

try: 

    direction = input("Which direction - f, b, l, r?")
    time.sleep(1)
    distance = int(input("Drive for ? seconds?"))

    if direction == "f":
        forward()
        time.sleep(distance)
        stop()
        time.sleep(1)
    if direction == "b":
        backward()
        time.sleep(distance)
        stop()
        time.sleep(1)
    if direction == "l":
        left()
        time.sleep(distance)
        stop()
        time.sleep(1)
    if direction == "r":
        right()
        time.sleep(distance)
        stop()
        time.sleep(1)

except KeyboardInterrupt:
       pass
#finally:
#    GPIO.cleanup()




