# ESPr One

https://www.switch-science.com/catalog/2620/

# OLED

https://www.amazon.co.jp/gp/product/B011KH7V8U/

* driver: SSD1306
* resolution: 128ｘ64

```
           D5   D4
3V3  GND  SCL  SDA   (ESPr One)
 |    |    |    |
 |    |    |    |
VDD  GND  SCK  SDA   (display)
```

# HC-SR04

http://akizukidenshi.com/catalog/g/gM-11009/

```
          (ESPr One)
 VCC  --- 5V
 GND  --- GND
 Trig --- D16
 Echo --- 5K1 ---+--- 10K --- GND
                 |
                D12
```

# piezo buzzer

```
piezo buzzer
   |    |
   |    |
  D14  GND  (ESPr One)
```

* D14 is connected to blue LED as well

# DS18B20

http://akizukidenshi.com/catalog/g/gI-05276/

```
  /^^^^^\
 +-------+
 |       |
 |DS18B20|
 +-------+
   | | |
   1 2 3

(DS18B20) 1 GND -> GND     (ESPr One)
(DS18B20) 2 DQ  -> IO2(D4) (ESPr One)
(DS18B20) 3 Vdd -> 3V3     (ESPr One)
```

* 10K resister of ESPr One IO2 is used for pull-up

# NJL7502 (ALS)

http://akizukidenshi.com/catalog/g/gI-02325/

```
(ESPr One)
   ADC(A0)
    |
    +---[K A]--- 3V3
    |   NJL7502
   100K
    |
   GND
```
