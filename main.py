from screen import oled
from config import CRIPTOS

import criptos
import time


while True:
    oled.fill(0)
    oled.text("Consultando", 1, 1, 1)
    oled.show()
    
    for moeda in CRIPTOS:
        cotacao = criptos.do_criptos(moeda)

        oled.fill(0)
        oled.text("Moeda: {}".format(cotacao['moeda']) , 1, 1, 1)
        oled.text("Compra: {}".format(cotacao['compra']), 1, 10, 1)
        oled.text("Venda: {}".format(cotacao['venda']), 1, 19, 1)
        oled.show()
        
        time.sleep(5)

