
# wificonnect.py
import network
from time import time
from time import sleep_ms
from gc import mem_free
import os


def wifi_connect():
    print("\nAvailable memory: %s Byte" % str(mem_free()))
    
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    start_time = time()

    if not wlan.isconnected():
        print("\nThe current device is not networked and is connecting ....")
        wlan.connect("WIFI-SSID", "WIFI-PASSWORD")
        while not wlan.isconnected():
            sleep_ms(500)
            if time() - start_time > 10:
                print("\nFail !!!")
                break


    if wlan.isconnected():
        IP_info = wlan.ifconfig()
        print("Wifi is connected with the following information:")
        print(" IP address : " + IP_info[0])
        print("Subnet mask : " + IP_info[1])
        print("    Gateway : " + IP_info[2])
        print("        DNS : " + IP_info[3])
        return "success"


