def do_connect():
    import network

    from config import WIFI_SSID, WIFI_PASSWORD

    wlan = network.WLAN(network.STA_IF)
    wlan.config(dhcp_hostname="CriptosIOT")
    wlan.active(True)

    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(WIFI_SSID, WIFI_PASSWORD)

        while not wlan.isconnected():
            pass

    print('network config: ', wlan.ifconfig())
    print('hostname: ', wlan.config('dhcp_hostname'))


if __name__ == "__main__":
    do_connect()
