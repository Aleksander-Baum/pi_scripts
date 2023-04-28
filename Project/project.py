import wiringpi
import time

TRIG_PIN = 0
ECHO_PIN = 1
MOTOR_PIN_1 = 3
MOTOR_PIN_2 = 4
MOTOR_PIN_3 = 6
MOTOR_PIN_4 = 9
pinLed = 10

wiringpi.wiringPiSetup()
wiringpi.pinMode(TRIG_PIN, wiringpi.OUTPUT)
wiringpi.pinMode(ECHO_PIN, wiringpi.INPUT)
wiringpi.pinMode(MOTOR_PIN_1, wiringpi.OUTPUT)
wiringpi.pinMode(MOTOR_PIN_2, wiringpi.OUTPUT)
wiringpi.pinMode(MOTOR_PIN_3, wiringpi.OUTPUT)
wiringpi.pinMode(MOTOR_PIN_4, wiringpi.OUTPUT)
WAVE_DRIVE_SEQUENCE = [[0,0,0,1], [0,0,1,0], [0,1,0,0], [1,0,0,0]]
RWAVE_DRIVE_SEQUENCE = [[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]]
wiringpi.pinMode(pinLed, 1)

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

def stepMotor(step, mode):
    if mode == 'wave':
        sequence = WAVE_DRIVE_SEQUENCE
    elif mode == 'rwave':
        sequence = RWAVE_DRIVE_SEQUENCE

    wiringpi.digitalWrite(MOTOR_PIN_1, sequence[step][0])
    wiringpi.digitalWrite(MOTOR_PIN_2, sequence[step][1])
    wiringpi.digitalWrite(MOTOR_PIN_3, sequence[step][2])
    wiringpi.digitalWrite(MOTOR_PIN_4, sequence[step][3])

# Test the distance function

sensor_on = True
ledcount = 0
while sensor_on == True:
    dist = distance()
    while dist >= 35:
        dist = distance()
        print(f"Measured Distance: {dist:.2f} cm")
        time.sleep(1.5)
    else:
        for i in range(200):
            stepMotor(i % 4, 'wave')
            time.sleep(0.01)  # wait 10ms between steps
        while ledcount <= 5:
            wiringpi.digitalWrite(pinLed, 0)
            time.sleep(0.5)
            wiringpi.digitalWrite(pinLed, 1)
            time.sleep(0.5)
            ledcount += 1
        for j in range(200):
            stepMotor(j % 4, 'rwave')
            time.sleep(0.01)
            wiringpi.digitalWrite(pinLed, 1)
        sensor_on = False