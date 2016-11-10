from ssd1306 import SSD1306_I2C
from machine import Pin, I2C
i2c = I2C(scl=Pin(5), sda=Pin(4))
i2c.start()
disp = SSD1306_I2C(128,64,i2c)
disp.poweron()
def show_strings(s):
    disp.fill(0)
    disp.text(s[0],0,0,1)
    disp.text(s[1],0,16,1)
    disp.text(s[2],0,32,1)
    disp.text(s[3],0,48,1)
    disp.show()
