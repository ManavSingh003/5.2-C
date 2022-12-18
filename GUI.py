from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

led1 = LED(27)
led2 = LED(17)
led3 = LED(18)

screen= Tk()
screen.title("LED TOGGLER")
def ledToggle1():
    ## for LED 1 ##
    if led1.is_lit:
        led1.off()
        Light1["text"] =  "Turn LED 1 on"
        
    else:
        led1.on()
        led2.off()
        led3.off()
        Light1["text"] =  "LED 1 on"
        Light2["text"] =  "LED 2 is off"
        Light3["text"] =  "LED 3 is off"
        
def ledToggle2():
      ## for LED 2 ##
    if led2.is_lit:
        led2.off()
        Light2["text"] =  "Turn LED 2 on"
        
    else:
        led2.on()
        led1.off()
        led3.off()
        Light2["text"] =  "LED 2 on"
        Light1["text"] =  "LED 1 is off"
        Light3["text"] =  "LED 3 is off"

def ledToggle3():   
        ## for LED 3 ##
    if led3.is_lit:
        led3.off()
        Light3["text"] =  "Turn LED 3 on"
        
    else:
        led3.on()
        led2.off()
        led1.off()
        Light3["text"] =  "LED 3 is on"
        Light1["text"] =  "LED 1 is off"
        Light2["text"] =  "LED 2 is off"
    
def ledToggle4():
    
    led3.off()
    led2.off()
    led1.off()
    Light3["text"] =  "LED 3 is off"
    Light1["text"] =  "LED 1 is off"
    Light2["text"] =  "LED 2 is off"

def ledToggle5():
    
    led3.on()
    led2.on()
    led1.on()
    Light3["text"] =  "LED 3 is on"
    Light1["text"] =  "LED 1 is on"
    Light2["text"] =  "LED 2 is on"

def close():
    RPi.GPIO.cleanup()
    screen.destroy()
    
Light1 = Button(screen, text = "Turn LED 1 ", command =ledToggle1,bg = "violet", height = 1, width =20)
Light2 = Button(screen, text = "Turn LED 2", command =ledToggle2,bg = "violet", height = 1, width =20)
Light3 = Button(screen, text = "Turn LED 3", command =ledToggle3,bg = "violet", height = 1, width =20)
LightOff = Button(screen, text = "Turn all LEDS Off", command =ledToggle4,bg = "violet", height = 1, width =20)
LightOn = Button(screen, text = "Turn all LEDS ON", command =ledToggle5,bg = "violet", height = 1, width =20)

Light1.grid(row=0, column =1)
Light2.grid(row=1, column =1)
Light3.grid(row=2, column =1)
LightOff.grid(row=0, column=2)
LightOn.grid(row=1, column=2)

exitButton = Button(screen, text = "EXIT(Close the Program)", command = close, bg = "red", height =1 , width = 20)
exitButton.grid(row = 2, column = 2)

