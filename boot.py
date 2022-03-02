

# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

from wificonnect import wifi_connect
import TimedTask

#上电需要过一次12点
wifi_connect() #连wifi
TimedTask.OnedayTimer() #开定时任务
