
#zzu.py 打卡
import ure
import urequests
import utime
import ujson

def zzu():  

  wechattiltle = "Information ZZUjksb"
  
  sta = zzu.auto_punch("学号", "密码")
  if sta == "success":
      wechatmessage =" ZZUjksb Success\n\n"
  else:
      wechatmessage =" ZZUjksb Failed, please try again\n\n"
  # utime.sleep(20) 
  

  zzu.Wechat(wechattiltle,wechatmessage)
  

def Wechat(title,content):   #打卡微信通知群组
  PPtoken= "pushplusID"
  api = "https://www.pushplus.plus/send"
  data = {
  "token": PPtoken,
  "title" : title,
  "content" : content,
  #"topic" : "群组代码",    群组推送使用
  }
  headers = {
  'Content-Type': 'application/json',
  }
  body=ujson.dumps(data).encode('utf-8')
  req = urequests.post(api, headers=headers, data=body)
  return req

 

def auto_punch(user_account, pwd):


    # 1.登录获取cookies~~~~~
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
        'referer': 'https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/first0?fun2=a',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    form = {
        "uid": user_account,  # 账号
        "upw": pwd,  # 密码
        "smbtn": "进入健康状况上报平台",
        "hh28": "750"  # 按照当前浏览器窗口大小计算
    }

    form1="uid="+user_account+"&upw="+pwd+"&smbtn=进入健康状况上报平台"+"&hhw8='750'"

    print("--准备登录请求--", user_account)
    r = urequests.post("https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/login", headers=headers,
                      data=form1)  # response为账号密码对应的ptopid和sid信息
    print("--成功登录请求--", user_account)

    text = r.text  # 解决乱码问题

    
    # 正则表达式获取ptopid和sid
    matchObj = ure.search(r'ptopid=(\w+)\&sid=(\w+)\"', text)
    ptopid = matchObj.group(1)
    sid = matchObj.group(2)
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
        'referer': 'https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/login',
    }
    r = urequests.get(
        "https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/jksb?ptopid=" + ptopid + "&sid=" + sid + "&fun2=")  # response里含有jksb对应的params

    text = r.text  # 解决乱码问题
    #print(text)
    print("--准备获取fun18--", user_account)
    start = text.find(r'<input type="hidden" name="fun18" value=') +41
    end = text.find(r'"', start) 
    fun18 =  text[ start : end ]
    print("--成功获取fun18："+fun18+"--", user_account)
    
    # 正则表达式获取ptopid和sid
    #matchObj = ure.search(r'ptopid=(\w+)\&sid=(\w+)\&', text)
    #ptopid = matchObj.group(1)
    #sid = matchObj.group(2)
    
    
    # 2.准备加载平台主页~~~~~
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
        'referer': 'https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/login' ,
    }
    
    print("--准备加载平台主页--", user_account)
    r = urequests.get("https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/jksb?ptopid=" + ptopid + "&sid=" + sid + "&fun2=",
                     headers=headers)  # response为jksb表单第一页
    print("--成功加载平台主页--", user_account)
    
    text = r.text  # 解决乱码问题
    
    # 正则表达式获取fun18和ptopid和sid
    
    
    #matchObj = ure.search(r'name=\"ptopid\" value=\"(\w+)\".+name=\"sid\" value=\"(\w+)\".+', text)
    #ptopid = matchObj.group(1)
    #sid = matchObj.group(2)
  

    # 3.进入提交表单页面~~~~~    
    form = {
        "day6": "b",
        "did": "1",
        "door": "",
        "men6": "a",
        "ptopid": ptopid,
        "sid": sid
    }
    form1="day6=b&did=1&door=&men6=a&ptopid="+ptopid+"&sid="+sid
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
        'Referer': 'https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/jksb?ptopid=' + ptopid1 + '&sid=' + sid1 + '&fun2=',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    print("--准备进入提交表单页面--", user_account)
    r = urequests.post("https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/jksb", headers=headers,
                      data=form1.encode('utf-8'))  # response为打卡的第二个表单
    print("--成功进入提交表单页面--", user_account)
    
    text = r.text  # 解决乱码问题
    #print(text)

    
    # 正则表达式获取ptopid和sid
    #matchObj = ure.search(r'name=\"ptopid\" value=\"(\w+)\".+name=\"sid\" value=\"(\w+)\"', text)
    #ptopid = matchObj.group(1)
    #sid = matchObj.group(2)

    form = {
        "myvs_1": "否",
        "myvs_2": "否",
        "myvs_3": "否",
        "myvs_4": "否",
        "myvs_5": "否",
        "myvs_6": "否",
        "myvs_7": "否",
        "myvs_8": "否",
        "myvs_9": "否",
        "myvs_10": "否",
        "myvs_11": "否",
        "myvs_12": "否",
        "myvs_13a": "41",  # 省份（自治区） 数字代表
        "myvs_13b": "4101",  # 直辖区/县 1101/1102
        "myvs_13c": "河南省.郑州市.科学大道100号",  # 详细地址
        "myvs_24": "否",  # 是否为当日返郑人员
        "myvs_26":"5",#疫苗3针 
        "myvs_14b": "",
        "memo22": "河南省.郑州市",
        "did": "2",
        "door": "",
        "day6": "",
        "men6": "a",
        "sheng6": "",
        "shi6": "",
        "fun3": "",
        "jingdu": "113.542812",
        "weidu": "34.830326",
        "fun18": fun18,
        "ptopid": ptopid,
        "sid": sid
    }
    form1="myvs_1=否&myvs_2=否&myvs_3=否&myvs_4=否&myvs_5=否&myvs_6=否&myvs_7=否&myvs_8=否&myvs_9=否&myvs_10=否&myvs_11=否&myvs_12=否&myvs_13a=41&myvs_13b=4101&myvs_13c=河南省.郑州市.科学大道100号&myvs_24=否&myvs_26=5&myvs_14b=&memo22=河南省.郑州市&did=2&door=&day6=&men6=a&sheng6=&shi6=&fun3=&jingdu=113.542812&weidu=34.830326&fun18="+fun18+"&ptopid="+ptopid+"&sid="+sid

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
        'Referer': 'https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/jksb',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    print("--准备提交打卡表单--", user_account)
    r = urequests.post("https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/jksb", data=form1.encode('utf-8'),
                      headers=headers)  # response为完成打卡页面
    print("--成功提交提交打卡表单--", user_account)

    text = r.text  # 解决乱码问题

    if "感谢你今日上报健康状况！" in text:
        print("--打卡成功--", user_account)

        return "success"
    else:
        print("--打卡失败--", user_account)
        print("--打卡失败返回的页面如下--", user_account)
        print(text)
        return "--打卡失败--"
    exit()




