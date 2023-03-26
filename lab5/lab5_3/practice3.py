import wiringpi
import time
import sys

pin2 = 2
pin1 = 1
pin0 = 0
pin5 = 5
pin_ldr = 7
pinSwitch = 8

wiringpi.wiringPiSetup()

wiringpi.pinMode(pin2, 1)
wiringpi.pinMode(pin1, 1)
wiringpi.pinMode(pin0, 1)
wiringpi.pinMode(pin5, 1)
wiringpi.pinMode(pin_ldr, wiringpi.INPUT)
wiringpi.pinMode(pinSwitch, 0)

threshold = 1000

while True:
    analog_value = wiringpi.analogRead(pin_ldr)

    if (analog_value > threshold) or (wiringpi.digitalRead(pinSwitch) == 0):
        print("light off")
        wiringpi.digitalWrite(pin2, 0)
        wiringpi.digitalWrite(pin1, 0)
        wiringpi.digitalWrite(pin0, 0)
        wiringpi.digitalWrite(pin5, 0)
    else:
        print("light off")
        print("light off")
        print("light off")
        print("light off")
        print("light on")
        print("light on")
        print("light on")
        print("light on")
        print("light on")
        print("light on")
        print("light on")
        print("light on")
        print("light on")
        print("light on")
        wiringpi.digitalWrite(pin2, 1)
        wiringpi.digitalWrite(pin1, 1)
        wiringpi.digitalWrite(pin0, 1)
        wiringpi.digitalWrite(pin5, 1)

    time.sleep(0.3)
    