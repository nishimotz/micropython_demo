from machine import ADC
adc = ADC(0)
def get_brightness():
    return int(adc.read())
