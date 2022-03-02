
#zzu.py 打卡
import ure
import urequests
import utime


def zzu():  #述胜   青林 长江 佳星 之铭 启尧 志远    晓杰 景军

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
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
  'Content-Type': 'application/x-www-form-urlencoded',
}
  data1="token="+PPtoken+"&title="+title+"&content="+content+"&topic=123"
  req = urequests.post(api, headers=headers, data=data1)
  return req

 

def auto_punch(user_account, pwd):

    # myvs_13a = city_code[0:2]  # 省份（自治区） 两位数字代表
    # myvs_13b = city_code[0:4]  # 地市 四位数字  若为直辖市这选择 直辖区/县1101/1102, 北京市 天津市 上海市 重庆市
    # myvs_13c = address  # 详细地址

    # 账号 密码
    # id = "学号"
    # pwd = "密码"

    # myvs_13a = "12"  # 省份（自治区） 两位数字代表
    # myvs_13b = "1201"  # 地市 四位数字  若为直辖市这选择 直辖区/县1101/1102, 北京市 天津市 上海市
    # myvs_13c = "天津地址"  # 详细地址
    # myvs_14 = "否"  # 是否为当日返郑人员

    # myvs_13a: "41"  # 省份（自治区） 数字代表
    # myvs_13b: "4101"  # 直辖区/县 1101/1102
    # myvs_13c: "河南省.郑州市.科学大道100号"

    # login
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
        'referer': 'https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/first0?fun2=a',
        'Content-Type': 'application/x-www-form-urlencoded',
        'x-forwarded-for': '219.155.76.199'
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
    # first6
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
    # jksb?with_params
    matchObj = ure.search(r'ptopid=(\w+)\&sid=(\w+)\&', text)
    ptopid = matchObj.group(1)
    sid = matchObj.group(2)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
        'referer': 'https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/login' ,
    }
    r = urequests.get("https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/jksb?ptopid=" + ptopid + "&sid=" + sid + "&fun2=",
                     headers=headers)  # response为jksb表单第一页
    ptopid1 = ptopid
    sid1 = sid
    text = r.text  # 解决乱码问题
    #print(text)
    # DONE
    matchObj = ure.search(
        r'name=\"ptopid\" value=\"(\w+)\".+name=\"sid\" value=\"(\w+)\".+', text)
    ptopid = matchObj.group(1)
    sid = matchObj.group(2)

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
    print("--准备加载平台主页--", user_account)
    r = urequests.post("https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/jksb", headers=headers,
                      data=form1.encode('utf-8'))  # response为打卡的第二个表单
    print("--成功加载平台主页--", user_account)
    
    text = r.text  # 解决乱码问题
    #print(text)
    # DONE
    matchObj = ure.search(r'name=\"ptopid\" value=\"(\w+)\".+name=\"sid\" value=\"(\w+)\"', text)
    ptopid = matchObj.group(1)
    sid = matchObj.group(2)

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
        "myvs_13": "g",  # 绿码
        "myvs_13a": "41",  # 省份（自治区） 数字代表
        "myvs_13b": "4101",  # 直辖区/县 1101/1102
        "myvs_13c": "河南省.郑州市.科学大道100号",  # 详细地址
        "myvs_24": "否",  # 是否为当日返郑人员
        "myvs_26":"2",#疫苗2针 
        "myvs_14b": "",
        "memo22": "河南省.郑州市",
        "did": "2",
        "door": "",
        "day6": "b",
        "men6": "a",
        "sheng6": "",
        "shi6": "",
        "fun3": "",
        "jingdu": "113.5359",
        "weidu": "34.8171",
        "ptopid": ptopid,
        "sid": sid
    }
    form1="myvs_1=否&myvs_2=否&myvs_3=否&myvs_4=否&myvs_5=否&myvs_6=否&myvs_7=否&myvs_8=否&myvs_9=否&myvs_10=否&myvs_11=否&myvs_12=否&myvs_13=g&myvs_13a=41&myvs_13b=4101&myvs_13c=河南省.郑州市.科学大道100号&myvs_24=否&myvs_26=2&myvs_14b=&memo22=河南省.郑州市&did=2&door=&day6=b&men6=a&sheng6=&shi6=&fun3=&jingdu=113.5359&weidu=34.8171&ptopid="+ptopid+"&sid="+sid

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
    #print(text)
    if "感谢你今日上报健康状况！" in text:
        print("--打卡成功--", user_account)
        # content = time.asctime(time.localtime(
        #     time.time())) + "--打卡成功--" + user_account
        # title = "打卡成功"
        # Wechat(title, content)
        return "success"
    elif '“地市”与“省份”选择相矛盾' in text:
        print("--打卡失败--地市与省份选择相矛盾--", user_account)
        return "--打卡失败--地市与省份选择相矛盾--"
    else:
        print("--打卡失败--", user_account)
        #print("--打卡失败返回的页面如下--", user_account)
        #print(text)
        # title = "打卡失败"
        # wechat.Wechat(title, text)
        return "--打卡失败--"
    exit()




