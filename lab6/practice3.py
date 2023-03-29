import wiringpi
import time

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

#Setup                               #We will use w16 as CE, not the default pin w15!
wiringpi.wiringPiSetup() 
wiringpi.pinMode(pin_CS_adc, 1)                 # Set ce to mode 1 ( OUTPUT )
wiringpi.wiringPiSPISetupMode(1, 0, 500000, 0)  #(channel, port, speed, mode)

while True:
    temperature_sum = 0
    for i in range(10): # get voltage to temperature 10 times
        ActivateADC()
        current_voltage = readadc(0) # read channel 0
        DeactivateADC()
        temperature_sum += ((3.3 * current_voltage * 100) / 1023) # calculate current coltage to temperature
        time.sleep(0.05)
    temperature_avg = temperature_sum / 10
    print("Temperature: {:.2f}°C".format(temperature_avg))
    time.sleep(1)