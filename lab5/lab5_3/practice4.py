import wiringpi
import time

wiringpi.wiringPiSetup()

LDR_PIN = 0
CAPACITOR_PIN = 1

wiringpi.pinMode(LDR_PIN, wiringpi.INPUT)
wiringpi.pinMode(CAPACITOR_PIN, wiringpi.OUTPUT)

wiringpi.digitalWrite(CAPACITOR_PIN, wiringpi.LOW)
time.sleep(0.1)

wiringpi.digitalWrite(CAPACITOR_PIN, wiringpi.HIGH)
while wiringpi.digitalRead(LDR_PIN) == wiringpi.LOW:
    pass

start_time = time.time()
while wiringpi.digitalRead(CAPACITOR_PIN) == wiringpi.HIGH:
    pass
charge_time = time.time() - start_time

print("%.3f" % charge_time)