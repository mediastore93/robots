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

while True: 

    direction = input("Which direction - f, b, l, r?")
    time.sleep(1)
    distance = input("Drive for ? seconds?")

        if direction == "f":
            forward()
            time.sleep(distance)
            stop()
        if direction == "b":
            backward()
            time.sleep(distance)
            stop()
        if direction == "l":
            left()
            time.sleep(distance)
            stop()
        if direction == "r":
            right()
            time.sleep(distance)
            stop()




