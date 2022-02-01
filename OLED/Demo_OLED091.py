from machine import I2C, Pin
from SSD1306 import SSD1306_I2C

i2c = I2C(scl=Pin(4), sda=Pin(5))
oled = SSD1306_I2C(128, 32, i2c)

oled.fill(0)
oled.text("HELLO!", 0, 0)
oled.show()