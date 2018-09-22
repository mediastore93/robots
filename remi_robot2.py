import explorerhat
from time import sleep
from guizero import App, PushButton


def forwards():
    explorerhat.motor.one.forward(100)
    explorerhat.motor.two.forward(100)
    sleep(2)
    explorerhat.motor.one.stop()
    explorerhat.motor.two.stop()


def backwards():
    explorerhat.motor.one.backward(100)
    explorerhat.motor.two.backward(100)
    sleep(2)
    explorerhat.motor.one.stop()
    explorerhat.motor.two.stop()
    
def left():
    explorerhat.motor.one.backward(33)
    explorerhat.motor.two.forward(33)
    sleep(1)
    explorerhat.motor.one.stop()
    explorerhat.motor.two.stop()

def right():
    explorerhat.motor.one.forward(33)
    explorerhat.motor.two.backward(33)
    sleep(1)
    explorerhat.motor.one.stop()
    explorerhat.motor.two.stop()

def right_half():
    explorerhat.motor.one.forward(33)
    explorerhat.motor.two.backward(33)
    sleep(0.5)
    explorerhat.motor.one.stop()
    explorerhat.motor.two.stop()

def left_half():
    explorerhat.motor.one.backward(33)
    explorerhat.motor.two.forward(33)
    sleep(0.5)
    explorerhat.motor.one.stop()
    explorerhat.motor.two.stop()

app = App("Buggy controller")

drive = PushButton(app, forwards, text="Forwards")
reverse = PushButton(app, backwards, text="Reverse")
left = PushButton(app, left, text="Left")
right = PushButton(app,right, text="right")
right_half = PushButton(app, right_half, text="right half")
left_half = PushButton(app, left_half, text="left half")

app.display()
