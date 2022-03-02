
# micropython 校时程序  (注意，必须先联网成功后，才能校时成功！！！)

import utime
import ntptime
import zzu


def OnedayTimer():

  from machine import Timer
  
  #开启定时器前先校准一下
  print("同步前本地时间：%s" %str(utime.localtime()))
  ntptime.NTP_DELTA = 3155644800    # 设置  UTC+8偏移时间（秒），不设置就是UTC0
  ntptime.host = 'ntp1.aliyun.com'  # 可选ntp服务器为阿里云服务器，默认是"pool.ntp.org"
  ntptime.settime()                 # 修改设备时间,到这就已经设置好了
  print("同步后本地时间：%s" %str(utime.localtime()))
  
  global TaskFlag #全局变量，标志是否打过卡
  TaskFlag=0
  
  timer = Timer(0)#调用定时器
  timer.init(period = 1000*60*30,mode = Timer.PERIODIC,callback = lambda x:display())
  #设置1000*60*10毫秒，定时器模式为一直运行，调用display（）

def display():
  print("同步前本地时间：%s" %str(utime.localtime()))
  
  ntptime.NTP_DELTA = 3155644800    # 设置  UTC+8偏移时间（秒），不设置就是UTC0
  ntptime.host = 'ntp1.aliyun.com'  # 可选ntp服务器为阿里云服务器，默认是"pool.ntp.org"
  ntptime.settime()                 # 修改设备时间,到这就已经设置好了
  
  print("同步后本地时间：%s" %str(utime.localtime()))
  
  #设定执行时间
  Set_hour = 5
  Set_min = 0
  (year, month, mday, hour, minute, second, weekday, yearday)=utime.localtime()
  #print(hour, minute)
  if hour==0 :     #零点设置任务标志
    global TaskFlag
    TaskFlag = 1
  
  if Set_hour<hour and Set_min<minute and TaskFlag:
    zzu.zzu()
    global TaskFlag
    TaskFlag = 0  #执行过就清除标志  



