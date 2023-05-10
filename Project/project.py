import wiringpi
import time
import json
import requests
from ch7_ClassLCD import LCD

def ActivateLCD():
    wiringpi.digitalWrite(pin_CS_lcd, 0)       # Actived LCD using CS
    time.sleep(0.000005)

def DeactivateLCD():
    wiringpi.digitalWrite(pin_CS_lcd, 1)       # Deactived LCD using CS
    time.sleep(0.000005)

PIN_OUT     =   {  
                'SCLK'  :   14,
                'DIN'   :   11,
                'DC'    :   9, 
                'CS'    :   15, #We will not connect this pin! --> we use w13
                'RST'   :   10,
                'LED'   :   6, #backlight   
}

TRIG_PIN = 0
ECHO_PIN = 1
MOTOR_PIN_1 = 3
MOTOR_PIN_2 = 4
MOTOR_PIN_3 = 12
MOTOR_PIN_4 = 7
pinLed = 5
pinSwitch1 = 2
pinSwitch2 = 15
pin_CS_lcd = 13

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
wiringpi.pinMode(pinSwitch1, 0)
wiringpi.pinMode(pinSwitch2, 0)
wiringpi.pinMode(pin_CS_lcd , 1)            # Set pin to mode 1 ( OUTPUT )
url = "http://muizenval.hub.ubeac.io/iotessaleksanderbaum"
uid = "iotessaleksanderbaum"

ActivateLCD()
lcd_1 = LCD(PIN_OUT)


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

current_time = time.localtime()
current_hour = str(f"{current_time.tm_hour}:{current_time.tm_min}")

trapclosed = False
trapstatus = 0
lcd_1.clear()
lcd_1.set_backlight(0)
triggercount = 0
while True:
    dist = distance()
    while dist >= 35 and trapclosed == False:
        ActivateLCD()
        lcd_1.clear()
        lcd_1.go_to_xy(0, 0)
        lcd_1.put_string(current_hour + '\nStatus: armed' + '\nTrigger count: ' + str(triggercount))
        lcd_1.refresh()
        DeactivateLCD()
        time.sleep(0.5)
        dist = distance()
        print(f"Measured Distance: {dist:.2f} cm")
        time.sleep(1)
        if(wiringpi.digitalRead(pinSwitch1) == 0):
            triggercount += 1
            trapstatus = 1
            ActivateLCD()
            lcd_1.clear()
            lcd_1.go_to_xy(0, 0)
            lcd_1.put_string(current_hour + '\nStatus: triggered' + '\nTrigger count: ' + str(triggercount))
            lcd_1.refresh()
            DeactivateLCD()
            trapclosed = True
            time.sleep(0.3)
            wiringpi.digitalWrite(pinLed,0)
            for i in range(200):
                stepMotor(i % 4, 'wave')
                time.sleep(0.01)  # wait 10ms between steps
    if dist < 35:
        triggercount += 1
        trapstatus = 1
        ActivateLCD()
        lcd_1.clear()
        lcd_1.go_to_xy(0, 0)
        lcd_1.put_string(current_hour + '\nStatus: triggered' + '\nTrigger count: ' + str(triggercount))
        lcd_1.refresh()
        DeactivateLCD()
        for i in range(200):
            stepMotor(i % 4, 'wave')
            time.sleep(0.01)  # wait 10ms between steps
            trapclosed = True
    while trapclosed == True:
        data= {
            "id": uid,
            "sensors":[{
                'id': 'trapstatus',
                'data': trapstatus
            },
            {   'id': 'triggercount',
                'data': triggercount
            }]
        }
        r = requests.post(url, verify=False, json=data)
        ActivateLCD()
        lcd_1.clear()
        lcd_1.go_to_xy(0, 0)
        lcd_1.put_string(current_hour + '\nStatus: triggered' + '\nTrigger count: ' + str(triggercount))
        lcd_1.refresh()
        DeactivateLCD()
        wiringpi.digitalWrite(pinLed, 0)
        time.sleep(0.2)
        wiringpi.digitalWrite(pinLed, 1)
        time.sleep(0.2)
        if(wiringpi.digitalRead(pinSwitch2) == 0):
            trapstatus = 0
            data= {
                "id": uid,
                "sensors":[{
                    'id': 'trapstatus',
                    'data': trapstatus
                },
                {   'id': 'triggercount',
                    'data': triggercount
                }]
            }
            r = requests.post(url, verify=False, json=data)
            ActivateLCD()
            lcd_1.clear()
            lcd_1.go_to_xy(0, 0)
            lcd_1.put_string(current_hour + '\nStatus: armed' + '\nTrigger count: ' + str(triggercount))
            lcd_1.refresh()
            DeactivateLCD()
            trapclosed = False
            time.sleep(0.3)
            wiringpi.digitalWrite(pinLed,1)
            for j in range(200):
                stepMotor(j % 4, 'rwave')
                time.sleep(0.01)
                wiringpi.digitalWrite(pinLed, 1)