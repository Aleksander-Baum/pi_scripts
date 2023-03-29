import wiringpi
import time
import sys

pin_CS_adc = 16  

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

wiringpi.wiringPiSetup() 
wiringpi.pinMode(pin_CS_adc, 1)                 # Set ce to mode 1 ( OUTPUT )
wiringpi.wiringPiSPISetupMode(1, 0, 500000, 0)  #(channel, port, speed, mode)

min_light = 0     # minimum light level that LDR can detect
max_light = 1023  # maximum light level that LDR can detect

while True:
    ActivateADC()
    current_light = readadc(1) # read channel 0
    DeactivateADC()
    current_light = (current_light - min_light) / (max_light - min_light) * 100 # calculate light incidence
    print("Current light: {:.2f}%".format(current_light))
    time.sleep(0.8)
    