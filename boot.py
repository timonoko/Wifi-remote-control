# This file is executed on every boot (including wake-boot from deepsleep)

def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('Jorpakko', 'Juhannusyona')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

do_connect() 

import gc
gc.collect()

import esp
esp.osdebug(None)

import os
print(os.listdir())

import uos, machine
#uos.dupterm(None, 1) # disable REPL on UART(0)

def ls():
    print(os.listdir())

import webrepl
webrepl.start()

import kauko



