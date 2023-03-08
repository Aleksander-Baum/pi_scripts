import time
import wiringpi
import sys

def blink(_pin2, _pin1, _pin0, _pin5):
    wiringpi.digitalWrite(_pin2, 1)
    wiringpi.digitalWrite(_pin1, 1)
    wiringpi.digitalWrite(_pin0, 1)
    wiringpi.digitalWrite(_pin5, 1)
    time.sleep(0.1)
    wiringpi.digitalWrite(_pin2, 0)
    wiringpi.digitalWrite(_pin1, 0)
    wiringpi.digitalWrite(_pin0, 0)
    wiringpi.digitalWrite(_pin5, 0)
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
    blink(pin2, pin1, pin0, pin5)

print("Done")