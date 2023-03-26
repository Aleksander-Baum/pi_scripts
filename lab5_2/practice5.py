import time
import wiringpi
import sys

def blink(_pin):
    wiringpi.digitalWrite(_pin, 1)
    time.sleep(0.1)
    wiringpi.digitalWrite(_pin, 0)
    time.sleep(0.1)

print("Start")
pinLed1 = 2
pinLed2 = 1
pinLed3 = 0
pinLed4 = 5
pinSwitch = 7
wiringpi.wiringPiSetup()
wiringpi.pinMode(pinLed1, 1)
wiringpi.pinMode(pinLed2, 1)
wiringpi.pinMode(pinLed3, 1)
wiringpi.pinMode(pinLed4, 1)
wiringpi.pinMode(pinSwitch, 0)

while True:
    if(wiringpi.digitalRead(pinSwitch) == 0):
        blink(pinLed1)
        blink(pinLed2)
        blink(pinLed3)
        blink(pinLed4)
    else:
        blink(pinLed4)
        blink(pinLed3)
        blink(pinLed2)
        blink(pinLed1)

print("Done")