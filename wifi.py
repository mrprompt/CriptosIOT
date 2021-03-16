from screen import oled


def do_connect():
    import network

    from config import WIFI_SSID, WIFI_PASSWORD

    wlan = network.WLAN(network.STA_IF)
    wlan.config(dhcp_hostname="CriptosIOT")
    wlan.active(True)

    if not wlan.isconnected():
        oled.fill(0)
        oled.text('Conectando...', 1, 1, 1)
        oled.show()
        
        wlan.connect(WIFI_SSID, WIFI_PASSWORD)

        while not wlan.isconnected():
            pass

    oled.fill(0)
    oled.text('Rede: ', wlan.ifconfig(), 1, 1, 1)
    oled.text('Host: ', wlan.config('dhcp_hostname'), 1, 8, 1)
    oled.show()


if __name__ == "__main__":
    do_connect()

