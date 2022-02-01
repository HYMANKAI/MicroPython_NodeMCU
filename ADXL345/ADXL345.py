import machine
import math
from machine import I2C, Pin

ADDRESS         = 0x53
DEVICE_ID       = 0x00 
THRESH_TAP      = 0x1D
OFSX            = 0x1E
OFSY            = 0x1F
OFSZ            = 0x20
DUR             = 0x21
Latent          = 0x22
Window          = 0x23 
THRESH_ACK      = 0x24
THRESH_INACT    = 0x25 
TIME_INACT      = 0x26
ACT_INACT_CTL   = 0x27     
THRESH_FF       = 0x28    
TIME_FF         = 0x29 
TAP_AXES        = 0x2A  
ACT_TAP_STATUS  = 0x2B 
BW_RATE         = 0x2C 
POWER_CTL       = 0x2D 

INT_ENABLE      = 0x2E
INT_MAP         = 0x2F
INT_SOURCE      = 0x30
DATA_FORMAT     = 0x31
DATA_X0         = 0x32
DATA_X1         = 0x33
DATA_Y0         = 0x34
DATA_Y1         = 0x35
DATA_Z0         = 0x36
DATA_Z1         = 0x37
FIFO_CTL        = 0x38
FIFO_STATUS     = 0x39

ADXL_READ       = 0x3B
ADXL_WRITE      = 0x3A

class ADXL345(object):
    def __init__(self, sclpin, sdapin):
        self.i2c = I2C(scl=Pin(sclpin), sda=Pin(sdapin), freq=100000)
        
    def Write_ADXL_REG(self, reg, dat):
        buf = bytearray(1)
        buf[0] = dat
        self.i2c.writeto_mem(ADDRESS, reg, buf)
        
    def Read_ADXL_REG(self, reg):
        t = self.i2c.readfrom_mem(ADDRESS, reg, 1)[0]
        return t
    
    def Read_ADXL_Len(self, reg, len, buffer):
        self.i2c.readfrom_mem_into(ADDRESS, reg, buffer)
    
    def ADXL_Init(self):
        res = self.Read_ADXL_REG(DEVICE_ID)
        if(res == 0xE5):
            self.Write_ADXL_REG(DATA_FORMAT, 0x2B);  # 中断低电平有效，13位全分辨率模式，16g量程
            self.Write_ADXL_REG(POWER_CTL, 0x28);    # 链接使能，测量模式
            self.Write_ADXL_REG(INT_ENABLE, 0x00);   # 不使用中断
            self.Write_ADXL_REG(OFSX, 0x00);
            self.Write_ADXL_REG(OFSY, 0x00);
            self.Write_ADXL_REG(OFSZ, 0x00);
    
    def Get_Raw_data(self):
        
        buf = bytearray(6)
        res = self.Read_ADXL_Len(DATA_X0, 6, buf)
        x = (buf[2] << 8) | buf[0]
        y = (buf[3] << 8) | buf[2]
        z = (buf[5] << 8) | buf[4]
        return x, y, z
    def Get_Result(self):
        
        buf = bytearray(6)
        res = self.Read_ADXL_Len(DATA_X0, 6, buf)
        x = (buf[2] << 8) | buf[0]
        y = (buf[3] << 8) | buf[2]
        z = (buf[5] << 8) | buf[4]
        
        t = x / math.sqrt(y*y + z*z)
        resx = math.atan(t)* 180 / 3.14
        
        t = y / math.sqrt(x*x + z*z)
        resy = math.atan(t)* 180 / 3.14
        
        t = math.sqrt(x*x + y*y) / z
        resz = math.atan(t)* 180 / 3.14
        return resx,resy,resz


