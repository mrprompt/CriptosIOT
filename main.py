from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

import criptos
import machine
import time
import sys
import os

i2c = I2C(-1, Pin(0), Pin(2))
oled = SSD1306_I2C(128, 32, i2c)

oled.text('iniciando...', 3, 3, 1)
oled.show()

while True:
    currencies = criptos.do_criptos()

    for currency in currencies:
       oled.fill(0)
       oled.text("Moeda: {}".format(currency['moeda']) , 1, 1, 1)
       oled.text("Compra: {}".format(currency['compra']), 1, 10, 1)
       oled.text("Venda: {}".format(currency['venda']), 1, 19, 1)
       oled.show()

       time.sleep(10)

