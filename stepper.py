import wiringpi as wp

# Define GPIO pins for stepper motor coils
coil_A_1_pin = 3
coil_A_2_pin = 4
coil_B_1_pin = 6
coil_B_2_pin = 9

# Define sequence of stepper motor steps
step_sequence = [
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1]
]

# Define number of steps per revolution
steps_per_rev = 512

# Initialize WiringPi library and set GPIO pins as output
wp.wiringPiSetupGpio()
wp.pinMode(coil_A_1_pin, wp.OUTPUT)
wp.pinMode(coil_A_2_pin, wp.OUTPUT)
wp.pinMode(coil_B_1_pin, wp.OUTPUT)
wp.pinMode(coil_B_2_pin, wp.OUTPUT)

# Define function to step motor forward or backward by specified number of steps
def step_motor(steps, direction):
    # Determine direction of rotation based on sign of step value
    if direction == 'forward':
        step_dir = 1
    elif direction == 'backward':
        step_dir = -1
    else:
        print("Invalid direction specified!")
        return

    # Calculate number of steps to take
    num_steps = abs(steps)

    # Loop through steps and set motor coils accordingly
    for i in range(num_steps):
        # Calculate index of current step in sequence
        step_idx = i % len(step_sequence)

        # Set motor coils according to current step in sequence
        wp.digitalWrite(coil_A_1_pin, step_sequence[step_idx][0])
        wp.digitalWrite(coil_A_2_pin, step_sequence[step_idx][1])
        wp.digitalWrite(coil_B_1_pin, step_sequence[step_idx][2])
        wp.digitalWrite(coil_B_2_pin, step_sequence[step_idx][3])

        # Delay to allow motor to move
        wp.delayMicroseconds(1000)

    # Turn off motor coils
    wp.digitalWrite(coil_A_1_pin, 0)
    wp.digitalWrite(coil_A_2_pin, 0)
    wp.digitalWrite(coil_B_1_pin, 0)
    wp.digitalWrite(coil_B_2_pin, 0)

# Example usage: rotate motor forward by one revolution (512 steps)
step_motor(steps_per_rev, 'forward')