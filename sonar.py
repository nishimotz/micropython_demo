from machine import Pin
import time
pin16 = Pin(16, Pin.OUT)
pin12 = Pin(12, Pin.IN)
def get_distance():
    signalon = signaloff = time.ticks_us()
    pin16.value(1)
    time.sleep(0.00001)
    pin16.value(0)
    while not pin12.value():
        signaloff = time.ticks_us()
    while pin12.value():
        signalon = time.ticks_us()
    return float(0.017 * (signalon - signaloff))
