def get_temperature():
    from machine import Pin
    from onewire import OneWire
    from ds18x20 import DS18X20
    ow = OneWire(Pin(2))
    ds = DS18X20(ow)
    roms = ds.scan()
    ds.convert_temp()
    return ds.read_temp(roms[0])
