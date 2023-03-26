import time
import wiringpi
import sys

print("Start")
relay1 = 0
relay2 = 1
pinSwitch = 0
wiringpi.wiringPiSetup()
wiringpi.pinMode(relay1, 1)
wiringpi.pinMode(relay2, 1)
wiringpi.pinMode(pinSwitch, 0)

while True:
    if(wiringpi.digitalRead(pinSwitch) == 1):
        wiringpi.pinMode(relay1, 1)
        wiringpi.pinMode(relay2, 0)
    else:
        wiringpi.pinMode(relay1, 0)
        wiringpi.pinMode(relay2, 1)

print("Done")