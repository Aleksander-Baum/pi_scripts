import time
import wiringpi 

# Define a new function to control the motor instead of the LEDs
def controlMotor(pin, speed):
    # Speed should be between 0 and 100
    wiringpi.softPwmWrite(pin, speed)

#SETUP
print("Start")
motor_pin = 2  # assuming the motor is connected to GPIO pin 2
pause_time = 0.02  # you can change this to slow down/speed up
wiringpi.wiringPiSetup() 

# Set pin as a softPWM output
wiringpi.softPwmCreate(motor_pin, 0, 100)

# Start PWM
wiringpi.softPwmWrite(motor_pin, 0)

try:
    while True:
        # Run the motor forwards for 10 seconds
        for i in range(0, 101):
            controlMotor(motor_pin, i)
            time.sleep(pause_time)
        time.sleep(10)

        # Stop the motor for 2 seconds
        controlMotor(motor_pin, 0)
        time.sleep(2)

except KeyboardInterrupt:
    controlMotor(motor_pin, 0)  # stop the motor
    print("\nDone")