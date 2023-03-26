import wiringpi
import time

TRIG_PIN = 4
ECHO_PIN = 5

wiringpi.wiringPiSetup()
wiringpi.pinMode(TRIG_PIN, wiringpi.OUTPUT)
wiringpi.pinMode(ECHO_PIN, wiringpi.INPUT)

def distance():
    wiringpi.digitalWrite(TRIG_PIN, wiringpi.HIGH)
    time.sleep(0.00001)
    wiringpi.digitalWrite(TRIG_PIN, wiringpi.LOW)

    while wiringpi.digitalRead(ECHO_PIN) == wiringpi.LOW:
        pulse_start = time.time()
    while wiringpi.digitalRead(ECHO_PIN) == wiringpi.HIGH:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17000
    return distance

# Test the distance function
while True:
    dist = distance()
    print(f"Measured Distance: {dist:.2f} cm")
    time.sleep(10)