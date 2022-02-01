import onewire,ds18x20
from machine import Pin

dat = machine.Pin(14)
ds = ds18x20.DS18X20(onewire.OneWire(dat))
roms = ds.scan()

ds.convert_temp()
for rom in roms:
    Temp = ds.read_temp(rom)
    
print(Temp,"°C")