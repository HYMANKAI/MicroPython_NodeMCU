import machine,time
from ADXL345 import ADXL345

adx=ADXL345(4,5) #(sclpin,sdapin)
adx.ADXL_Init()

while True:
    acc = adx.Get_Raw_data()
    print('result:',acc[0],acc[1],acc[2])
    time.sleep_ms(200)
