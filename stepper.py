import time
import wiringpi
import sys

# GPIO pins connected to the stepper motor driver
STEP_PIN = 0
DIR_PIN = 1

# Set up the WiringPi library
wiringpi.wiringPiSetup()

# Set up the GPIO pins as output
wiringpi.pinMode(STEP_PIN, wiringpi.OUTPUT)
wiringpi.pinMode(DIR_PIN, wiringpi.OUTPUT)

# Set the direction of the stepper motor
wiringpi.digitalWrite(DIR_PIN, wiringpi.HIGH)

# Define the number of steps per revolution and delay between steps
steps_per_revolution = 200
delay = 0.01

# Function to move the stepper motor a specified number of steps
def move_steps(num_steps):
    # Move the motor one step at a time in the specified direction
    for i in range(num_steps):
        wiringpi.digitalWrite(STEP_PIN, wiringpi.HIGH)
        time.sleep(delay)
        wiringpi.digitalWrite(STEP_PIN, wiringpi.LOW)
        time.sleep(delay)

# Move the stepper motor 200 steps in one direction
move_steps(steps_per_revolution)

# Move the stepper motor 200 steps in the opposite direction
wiringpi.digitalWrite(DIR_PIN, wiringpi.LOW)
move_steps(steps_per_revolution)