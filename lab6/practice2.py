import wiringpi
import time

def ActivateADC ():
    wiringpi.digitalWrite(pin_CS_adc, 0)       # Actived ADC using CS
    time.sleep(0.000005)

def DeactivateADC():
    wiringpi.digitalWrite(pin_CS_adc, 1)       # Deactived ADC using CS
    time.sleep(0.000005)

def readadc(adcnum):                           # Read analog input data from ADC
    if ((adcnum > 7) or (adcnum < 0)): 
        return -1 
    revlen, recvData = wiringpi.wiringPiSPIDataRW(1, bytes([1,(8+adcnum)<<4,0]))
    time.sleep(0.000005)
    adcout = ((recvData[1]&3) << 8) + recvData[2] 
    
    return adcout  

#Setup
print("Start")
pin0 = 0                                        # Set led1 pin to 0
pin1 = 1                                        # Set led2 pin to 1
wiringpi.wiringPiSetup()
wiringpi.pinMode(pin0, 1)                       # Turn on led1
wiringpi.pinMode(pin1, 1)                       # Turn on led2
pin_CS_adc = 16                                 #We will use w16 as CE, not the default pin w15!
wiringpi.wiringPiSetup() 
wiringpi.pinMode(pin_CS_adc, 1)                 # Set ce to mode 1 ( OUTPUT )
wiringpi.wiringPiSPISetupMode(1, 0, 500000, 0)  #(channel, port, speed, mode)

#Main
try:
    while True:
        tmp0_val = 0 # will also store channel 0 data
        tmp1_val = 1 # ^^ channel 1 data
        ActivateADC()
        tmp0 = readadc(0) # read channel 0
        DeactivateADC()
        ActivateADC()
        tmp1 = readadc(1) # read channel 0
        DeactivateADC()
        if (abs(tmp0 - tmp0_val) > 5): # set hysteresis gap to channel 0 input
            tmp0_val = tmp0
        if (abs(tmp1 - tmp1_val) > 5): # ^^ to channel 1 input
            tmp1_val = tmp1
        if (tmp0_val > tmp1_val):
            wiringpi.digitalWrite(pin0, 1) # activate leds
            wiringpi.digitalWrite(pin1, 0)
            print("LED 1 ACTIVE")
        elif (tmp1_val > tmp0_val):
            wiringpi.digitalWrite(pin0, 0) # activate leds
            wiringpi.digitalWrite(pin1, 1)
            print("LED 2 ACTIVE")
        time.sleep(1)

except KeyboardInterrupt:
    DeactivateADC()
    print("\nProgram terminated")