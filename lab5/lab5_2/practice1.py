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
        print("led blinking")
        time.sleep(0.3)
        wiringpi.digitalWrite(pinLed, 1)
    else:
        print("LED not flashing")
        time.sleep(0.3)
        wiringpi.digitalWrite(pinLed, 0)

print("Done")