import wiringpi
import time
import sys

pin_ldr = 1

wiringpi.wiringPiSetup()

wiringpi.pinMode(pin_ldr, wiringpi.INPUT)

threshold = 1000

while True:
    analog_value = wiringpi.analogRead(pin_ldr)

    if analog_value > threshold:
        print("light")
    else:
        print("dark")
    time.sleep(0.3)
    