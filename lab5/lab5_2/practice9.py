import wiringpi
import time

MOTOR_PIN_1 = 3
MOTOR_PIN_2 = 4
MOTOR_PIN_3 = 6
MOTOR_PIN_4 = 9
BUTTON_PIN = 1

# Define the sequence of steps for each mode
FULL_STEP_SEQUENCE = [[1,1,0,0], [0,1,1,0], [0,0,1,1], [1,0,0,1]]
REVERSE_STEP_SEQUENCE = [[1,0,0,1], [0,0,1,1], [0,1,1,0], [1,1,0,0]]

def stepMotor(step, mode):
    if mode == 'full':
        sequence = FULL_STEP_SEQUENCE
    elif mode == 'reverse':
        sequence = REVERSE_STEP_SEQUENCE

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

# Set up button pin as input with pull-up resistor
wiringpi.pinMode(BUTTON_PIN, wiringpi.INPUT)
wiringpi.pullUpDnControl(BUTTON_PIN, wiringpi.PUD_UP)

# Initialize variables
step = 0
mode = 'full'

while True:
    # Check for button press
    if wiringpi.digitalRead(BUTTON_PIN) == wiringpi.LOW:
        # Button is pressed, toggle mode
        if mode == 'full':
            mode = 'reverse'
        else:
            mode = 'full'
        step = 0  # Reset step counter
    
    # Step the motor
    stepMotor(step % 4, mode)
    step += 1
    time.sleep(0.01)  # wait 10ms between steps