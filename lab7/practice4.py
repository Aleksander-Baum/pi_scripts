import time
import wiringpi
import spidev
from ch7_ClassLCD import LCD
from PIL import Image

def ActivateLCD():
    wiringpi.digitalWrite(pin_CS_lcd, 0)       # Actived LCD using CS
    time.sleep(0.000005)

def DeactivateLCD():
    wiringpi.digitalWrite(pin_CS_lcd, 1)       # Deactived LCD using CS
    time.sleep(0.000005)

def ActivateADC ():
    wiringpi.digitalWrite(pin_CS_adc, 0)       # Actived ADC using CS
    time.sleep(0.000005)

def DeactivateADC():
    wiringpi.digitalWrite(pin_CS_adc, 1)       # Deactived ADC using CS
    time.sleep(0.000005)

PIN_OUT     =   {  
                'SCLK'  :   14,
                'DIN'   :   11,
                'DC'    :   9, 
                'CS'    :   15, #We will not connect this pin! --> we use w13
                'RST'   :   10,
                'LED'   :   6, #backlight   
}

def readadc(adcnum): 
    if ((adcnum > 7) or (adcnum < 0)): 
        return -1 
    revlen, recvData = wiringpi.wiringPiSPIDataRW(1, bytes([1,(8+adcnum)<<4,0]))
    time.sleep(0.000005)
    adcout = ((recvData[1]&3) << 8) + recvData[2] 
    
    return adcout  

#IN THIS CODE WE USE W13 (PIN 22) AS CHIP SELECT
pin_CS_lcd = 13
pin_CS_adc = 16                                 #We will use w16 as CE, not the default pin w15!
wiringpi.wiringPiSetup() 
wiringpi.wiringPiSPISetupMode(1, 0, 400000, 0)  #(channel, port, speed, mode)
wiringpi.pinMode(pin_CS_lcd , 1)            # Set pin to mode 1 ( OUTPUT )
wiringpi.pinMode(pin_CS_adc, 1)             # Set ce to mode 1 ( OUTPUT )
ActivateLCD()
lcd_1 = LCD(PIN_OUT)

i=90
image = Image.open("imagenokia.jpg").convert('1')
image1 = image.tobytes() # import and covert image to bitmap
try:
    lcd_1.clear()
    lcd_1.set_backlight(1)
    while True:
        ActivateLCD()
        LCD.draw_image(lcd_1, image1, 84, 48, x = 0, y = 0) # draw image on LCD
        lcd_1.refresh()
        DeactivateLCD()
        time.sleep(1)
        lcd_1.clear()
except KeyboardInterrupt:
    lcd_1.clear()
    lcd_1.refresh()
    lcd_1.set_backlight(1)
    DeactivateLCD()
    print("\nProgram terminated")


