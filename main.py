from display import show_strings
from machine import Pin, I2C
from temperature import get_temperature
import sound
from light import get_brightness
_ = get_temperature()

pin0 = Pin(0, Pin.IN)
#pin0.irq(trigger=Pin.IRQ_FALLING, handler=lambda p: print(p))

def startup():
    tp = get_temperature()
    s = [
        'MicroPython',
        'light: %d' % get_brightness(),
        'temp: %.1f' % tp
    ]
    if tp < 18.0:
        s.append("it's cold")
    elif tp > 20.0:
        s.append("it's warm")
    else:
        s.append('good condition')
    show_strings(s)

startup()
sound.rising_sound()

import time
while True:
    for _ in range(100):
        time.sleep(0.1)
        if pin0.value() == 0:
            print('user button pressed')
            import sys
            sys.exit()
    import game
    game.main()
