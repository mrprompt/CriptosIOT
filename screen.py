from machine import Pin, I2C
from ssd1306 import SSD1306_I2C


i2c = I2C(-1, Pin(0), Pin(2))
oled = SSD1306_I2C(128, 32, i2c)

oled.text('iniciando...', 3, 3, 1)
oled.show()
