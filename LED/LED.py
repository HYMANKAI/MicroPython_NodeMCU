from machine import Pin

class LED(object):
    def __init__(self, lpin):
        self.led = Pin(lpin, Pin.OUT)
        self.led.value(1)

    def on(self):
        self.led.value(0)

    def off(self):
        self.led.value(1)

    def rvs(self):
        if self.led.value():
            self.led.value(0)
        else:
            self.led.value(1)

    def breathe(self):
        import machine
        import utime

        p = machine.Pin(2)
        pwm = machine.PWM(p)
        pwm.freq(500)
        while True:
            for duty in range(0, 1023, 10):
                pwm.duty(duty)
                utime.sleep_ms(20)
            for duty in range(1023, 0, -10):
                pwm.duty(duty)
                utime.sleep_ms(20)
