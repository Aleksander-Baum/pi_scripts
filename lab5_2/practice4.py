import time
import wiringpi
import sys

print("Start")
pinLed = 2
pinSwitch = 1
wiringpi.wiringPiSetup()
wiringpi.pinMode(pinLed, 1)
wiringpi.pinMode(pinSwitch, 0)

while True:
    if(wiringpi.digitalRead(pinSwitch) == 0):
        for x in range(3):
            wiringpi.pinMode(pinLed, 1)
            time.sleep(0.5)
            wiringpi.pinMode(pinLed, 0)
            time.sleep(0.5)
        for y in range(3):
            wiringpi.pinMode(pinLed, 1)
            time.sleep(1.5)
            wiringpi.pinMode(pinLed, 0)
            time.sleep(1.5)
        for z in range(3):
            wiringpi.pinMode(pinLed, 1)
            time.sleep(0.5)
            wiringpi.pinMode(pinLed, 0)
            time.sleep(0.5)
    else:
        wiringpi.pinMode(pinLed, 0)

print("Done")