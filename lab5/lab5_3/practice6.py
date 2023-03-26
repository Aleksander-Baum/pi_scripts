import wiringpi
import time

TRIG_PIN = 4
ECHO_PIN = 5
MOTOR_PIN_1 = 8
MOTOR_PIN_2 = 11
MOTOR_PIN_3 = 12
MOTOR_PIN_4 = 14
pin1 = 8
pin2 = 11
pin3 = 12
pin4 = 14

FULL_STEP_SEQUENCE = [[1,1,0,0], [0,1,1,0], [0,0,1,1], [1,0,0,1]]

def stepMotor(step, mode):
    if mode == 'full':
        sequence = FULL_STEP_SEQUENCE

    # Set the pins according to the current step
    wiringpi.digitalWrite(MOTOR_PIN_1, sequence[step][0])
    wiringpi.digitalWrite(MOTOR_PIN_2, sequence[step][1])
    wiringpi.digitalWrite(MOTOR_PIN_3, sequence[step][2])
    wiringpi.digitalWrite(MOTOR_PIN_4, sequence[step][3])

wiringpi.wiringPiSetup()
wiringpi.pinMode(TRIG_PIN, wiringpi.OUTPUT)
wiringpi.pinMode(ECHO_PIN, wiringpi.INPUT)
wiringpi.pinMode(MOTOR_PIN_1, wiringpi.OUTPUT)
wiringpi.pinMode(MOTOR_PIN_2, wiringpi.OUTPUT)
wiringpi.pinMode(MOTOR_PIN_3, wiringpi.OUTPUT)
wiringpi.pinMode(MOTOR_PIN_4, wiringpi.OUTPUT)


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
step = 0
mode = 'full'

while True:
    dist = distance()
    if (dist > 30):
        wiringpi.digitalWrite(pin1, 0)
        wiringpi.digitalWrite(pin2, 0)
        wiringpi.digitalWrite(pin3, 0)
        wiringpi.digitalWrite(pin4, 0)
        print("safe")
        print(f"Difference: {dist:.2f} cm")
        time.sleep(2.5)

    else:
        print("alarm")
        print(f"Difference: {dist:.2f} cm")
        for i in range(500):
            stepMotor(i % 4, 'full')
            time.sleep(0.01)  # wait 10ms between steps