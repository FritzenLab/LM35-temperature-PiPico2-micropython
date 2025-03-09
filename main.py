# with ideas from: https://randomnerdtutorials.com/raspberry-pi-pico-analog-inputs-micropython/
from machine import Pin, ADC
import time

initialtime= time.ticks_ms() #https://docs.micropython.org/en/latest/library/time.html
LM35 = ADC(Pin(26)) #ADC0

       
while True:
       
    currenttime= time.ticks_ms() #Every time it passes here, gets the current time
    if time.ticks_diff(time.ticks_ms(), initialtime) > 1000: # this IF will be true every 2000 ms
        initialtime= time.ticks_ms() #update with the "current" time
         
        LM35raw = LM35.read_u16() # read value, 0-65535 across voltage range 0.0v - 3.3v
        # line below converts from 16bit to volts, then rounds it to 3 places then
        # multiplies by 100 to convert from milivolts to degrees Celsius
        LM35C= round((LM35raw * 3.3 / 65535),3)*100
        print(LM35C, end= "")
        print(" C")
            
