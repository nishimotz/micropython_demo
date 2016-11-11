from machine import Pin
import time
pin16 = Pin(16, Pin.OUT)
pin12 = Pin(12, Pin.IN)
def get_distance():
    start = signalon = signaloff = time.ticks_us()
    pin16.value(1)
    time.sleep(0.00001)
    pin16.value(0)
    while not pin12.value():
        signaloff = time.ticks_us()
        if signaloff - start > 20000:
            break
    while pin12.value():
        signalon = time.ticks_us()
        if signalon - signaloff > 20000:
            break
    try:
        return float(0.017 * (signalon - signaloff))
    except NameError:
        return 0.0
