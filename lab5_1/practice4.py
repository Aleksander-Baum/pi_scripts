import time
import wiringpi
import sys

def blink(_pin):
    wiringpi.digitalWrite(_pin, 1)
    time.sleep(0.1)
    wiringpi.digitalWrite(_pin, 0)
    time.sleep(0.1)

print("Start")
pin2 = 2
pin1 = 1
pin0 = 0
pin5 = 5
wiringpi.wiringPiSetup()
wiringpi.pinMode(pin2, 1)
wiringpi.pinMode(pin1, 1)
wiringpi.pinMode(pin0, 1)
wiringpi.pinMode(pin5, 1)

while True:
    blink(pin2)
    blink(pin1)
    blink(pin0)
    blink(pin5)
    blink(pin0)
    blink(pin1)

print("Done")