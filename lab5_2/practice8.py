import wiringpi
import time

MOTOR_PIN_1 = 3
MOTOR_PIN_2 = 4
MOTOR_PIN_3 = 6
MOTOR_PIN_4 = 9

# Define the sequence of steps for each mode
FULL_STEP_SEQUENCE = [[1,1,0,0], [0,1,1,0], [0,0,1,1], [1,0,0,1]]

def stepMotor(step, mode):
        sequence = FULL_STEP_SEQUENCE

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

# Example usage: move motor 200 steps in full step mode
for i in range(500):
    stepMotor(i % 4, 'full')
    time.sleep(0.01)  # wait 10ms between steps