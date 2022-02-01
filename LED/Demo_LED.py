# Function operation

import time
from LED import LED
led = LED(2)

while True:
    time.sleep_ms(200)
    led.on()
    time.sleep_ms(200)
    led.off()
    time.sleep_ms(200)
    led.rvs()
    
    
# Original operation

# import machine,time
# from machine import Pin
# led = Pin(2,Pin.OUT)
# 
# while True:
#     time.sleep_ms(200)
#     led.value(0)
#     time.sleep_ms(200)
#     led.value(1)
#     time.sleep_ms(200)
#     if led.value():
#         led.value(0)
#     else:
#         led.value(1)
        