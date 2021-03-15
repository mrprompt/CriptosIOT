# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)

import gc
gc.collect()

import wifi
wifi.do_connect()

import ntp
ntp.do_ntp()

import webrepl
webrepl.start()
