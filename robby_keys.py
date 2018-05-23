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




direction = input("Which direction - f, b, l, r?")
time.sleep(1)
distance = input("How far?")
if direction == "f" and distance == "1":
    forward()
    time.sleep(3)
    stop()
        


#forward()
#time.sleep(2)
#stop()

