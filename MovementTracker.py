import machine
import time

led = machine.Pin('LED', machine.Pin.OUT)

led.value(1)

time.sleep(2)

led.value(0)