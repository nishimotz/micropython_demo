def sound_loop(r, tick=0.15):
    import time
    from machine import Pin, PWM
    pin14 = Pin(14, Pin.OUT)
    pwm14 = PWM(pin14)
    pwm14.duty(0)
    for f in r:
        if f:
            pwm14.freq(f)
            pwm14.duty(512)
        else:
            pwm14.duty(0)
        time.sleep(tick)
    pwm14.duty(0)

notes_freq = [130,164,195,261]

def rising_sound():
    sound_loop(notes_freq)

def falling_sound():
    sound_loop(reversed(notes_freq))
