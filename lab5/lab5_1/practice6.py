import time
import wiringpi
import sys

def blink(_pin):
    for x in range(3):
        wiringpi.digitalWrite(_pin, 1)
        time.sleep(0.5)
        wiringpi.digitalWrite(_pin, 0)
        time.sleep(0.5)
    for y in range(3):
        wiringpi.digitalWrite(_pin, 1)
        time.sleep(1.5)
        wiringpi.digitalWrite(_pin, 0)
        time.sleep(1.5)
    for z in range(3):
        wiringpi.digitalWrite(_pin, 1)
        time.sleep(0.5)
        wiringpi.digitalWrite(_pin, 0)
        time.sleep(0.5)


print("Start")
pin = 2
wiringpi.wiringPiSetup()
wiringpi.pinMode(pin, 1)

while True:
    blink(pin)

print("Done")