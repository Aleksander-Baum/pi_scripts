import wiringpi
import time

MOTOR_PIN_1 = 3
MOTOR_PIN_2 = 4
MOTOR_PIN_3 = 6
MOTOR_PIN_4 = 9

# Define the sequence of steps for each mode
WAVE_DRIVE_SEQUENCE = [[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]]
FULL_STEP_SEQUENCE = [[1,1,0,0], [0,1,1,0], [0,0,1,1], [1,0,0,1]]

def stepMotor(step, mode):
    if mode == 'wave':
        sequence = WAVE_DRIVE_SEQUENCE
    elif mode == 'full':
        sequence = FULL_STEP_SEQUENCE
    else:
        raise ValueError('Invalid mode')

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

# Example usage: move motor 200 steps in wave drive mode
for i in range(2000):
    stepMotor(i % 4, 'wave')
    time.sleep(0.01)  # wait 10ms between steps

# Reset motor to initial position
for i in range(2000):
    stepMotor((3-i) % 4, 'wave')
    time.sleep(0.01)  # wait 10ms between steps

# # Example usage: move motor 200 steps in full step mode
# for i in range(200):
#     stepMotor(i % 4, 'full')
#     time.sleep(0.01)  # wait 10ms between steps

# # Reset motor to initial position
# for i in range(4):
#     stepMotor(i, 'full')
#     time.sleep(0.01)  # wait 10ms between steps