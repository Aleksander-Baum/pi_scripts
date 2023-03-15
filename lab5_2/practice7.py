import wiringpi
import time

MOTOR_PIN_1 = 3
MOTOR_PIN_2 = 4
MOTOR_PIN_3 = 6
MOTOR_PIN_4 = 9

# Define the sequence of steps for each mode
WAVE_DRIVE_SEQUENCE = [[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]]

def stepMotor(step, mode):
    sequence = WAVE_DRIVE_SEQUENCE

    # Set the pins according to the current step
    wiringpi.digitalWrite(MOTOR_PIN_1, sequence[step][0])
    wiringpi.digitalWrite(MOTOR_PIN_2, sequence[step][1])
    wiringpi.digitalWrite(MOTOR_PIN_3, sequence[step][2])
    wiringpi.digitalWrite(MOTOR_PIN_4, sequence[step][3])

# Set up WiringPi
wiringpi.wiringPiSetup()

# Set up motor pins as outputs
wiringpi.pinMode(MOTOR_PIN_1, wiringpi.OUTPUT)
wiringpi.pinMode(MOTOR_PIN_2, wiringpi.OUTPUT)
wiringpi.pinMode(MOTOR_PIN_3, wiringpi.OUTPUT)
wiringpi.pinMode(MOTOR_PIN_4, wiringpi.OUTPUT)

for i in range(500):
    stepMotor(i % 4, 'wave')
    time.sleep(0.01)  # wait 10ms between steps