import machine
import time

led = machine.Pin('LED', machine.Pin.OUT)

led.value(0)