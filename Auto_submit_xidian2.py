# -*- coding: UTF-8 -*-
import requests


def main(id='main'):


    #######################################

    USERNAME = 'XXXXXXX'#学号
    PASSWORD = 'XXXXXXX'#密码
    FORMDATA = 'sfzx=1&tw=2&area=%E9%99%95%E8%A5%BF%E7%9C%81%20%E8%A5%BF%E5%AE%89%E5%B8%82%20%E9%95%BF%E5%AE%89%E5%8C%BA&city=%E8%A5%BF%E5%AE%89%E5%B8%82&province=%E9%99%95%E8%A5%BF%E7%9C%81&address=%E9%99%95%E8%A5%BF%E7%9C%81%E8%A5%BF%E5%AE%89%E5%B8%82%E9%95%BF%E5%AE%89%E5%8C%BA%E9%83%AD%E6%9D%9C%E8%A1%97%E9%81%93%E4%B8%89%E4%BB%81%E8%B7%AF%E9%82%93%E5%BA%97%E5%8C%97%E6%9D%91&geo_api_info=%7B%22type%22%3A%22complete%22%2C%22position%22%3A%7B%22Q%22%3A34.154003363716%2C%22R%22%3A108.85532443576403%2C%22lng%22%3A108.855324%2C%22lat%22%3A34.154003%7D%2C%22location_type%22%3A%22html5%22%2C%22message%22%3A%22Get%20ipLocation%20failed.Get%20geolocation%20success.Convert%20Success.Get%20address%20success.%22%2C%22accuracy%22%3A6026%2C%22isConverted%22%3Atrue%2C%22status%22%3A1%2C%22addressComponent%22%3A%7B%22citycode%22%3A%22029%22%2C%22adcode%22%3A%22610116%22%2C%22businessAreas%22%3A%5B%7B%22name%22%3A%22%E9%83%AD%E6%9D%9C%22%2C%22id%22%3A%22610116%22%2C%22location%22%3A%7B%22Q%22%3A34.160655%2C%22R%22%3A108.86978899999997%2C%22lng%22%3A108.869789%2C%22lat%22%3A34.160655%7D%7D%5D%2C%22neighborhoodType%22%3A%22%22%2C%22neighborhood%22%3A%22%22%2C%22building%22%3A%22%22%2C%22buildingType%22%3A%22%22%2C%22street%22%3A%22%E9%83%AD%E6%9D%9C%E5%8D%97%E8%A1%97%22%2C%22streetNumber%22%3A%22198%E5%8F%B7%22%2C%22country%22%3A%22%E4%B8%AD%E5%9B%BD%22%2C%22province%22%3A%22%E9%99%95%E8%A5%BF%E7%9C%81%22%2C%22city%22%3A%22%E8%A5%BF%E5%AE%89%E5%B8%82%22%2C%22district%22%3A%22%E9%95%BF%E5%AE%89%E5%8C%BA%22%2C%22towncode%22%3A%22610116002000%22%2C%22township%22%3A%22%E9%83%AD%E6%9D%9C%E8%A1%97%E9%81%93%22%7D%2C%22formattedAddress%22%3A%22%E9%99%95%E8%A5%BF%E7%9C%81%E8%A5%BF%E5%AE%89%E5%B8%82%E9%95%BF%E5%AE%89%E5%8C%BA%E9%83%AD%E6%9D%9C%E8%A1%97%E9%81%93%E4%B8%89%E4%BB%81%E8%B7%AF%E9%82%93%E5%BA%97%E5%8C%97%E6%9D%91%22%2C%22roads%22%3A%5B%5D%2C%22crosses%22%3A%5B%5D%2C%22pois%22%3A%5B%5D%2C%22info%22%3A%22SUCCESS%22%7D&sfcyglq=0&sfyzz=0&qtqk=&ymtys=0'
    WXPUSHER_appToken='AT_XXXXXXX'
    WXPUSHER_uid='UID_XXXXXXX'
    ###   ATTENTION！！！
    #数据获取方式：浏览器中打开晨午晚检-》（登录）==》右键审查元素（或F12）==》网络==》填写表格后点击提交==》网络中出现一个新名称：save ==》点击该名称==》右侧找到查询字符串参数==》点击 查看源 ==》复制所有数据
    #WXPUSHER网站可以获取appToken和uid
    #######################################


    url = "https://xxcapp.xidian.edu.cn/uc/wap/login?"
    resp = requests.get(url)
    eai_sess = resp.headers['Set-Cookie'].split(";")[0]

    #登录，获取cookie

    url2 = "https://xxcapp.xidian.edu.cn/uc/wap/login/check"
    print("账号:" + USERNAME)
    print("密码:" + PASSWORD)
    data = "username=" + USERNAME + "&password=" + PASSWORD
    headers = {
        "Host": "xxcapp.xidian.edu.cn",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "Origin": "https://xxcapp.xidian.edu.cn",
        "Connection": "keep-alive",
        "Referer": "https://xxcapp.xidian.edu.cn/uc/wap/login?",
        "Cookie": eai_sess
    }
    resp2 = requests.post(url2, data=data, headers=headers)
    #print(resp2.text)
    if "操作成功" in resp2.text:
        print("登录成功，已获取cookie")
    else:
        print("登录失败！")

    #上报数据
    load_data = FORMDATA
    url = "https://xxcapp.xidian.edu.cn/xisuncov/wap/open-report/save"
    login_cookies = eai_sess
    headers = {
        "Host": "xxcapp.xidian.edu.cn",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:72.0) Gecko/20100101 Firefox/72.0 micromessenger",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "Origin": "https://xxcapp.xidian.edu.cn",
        "Connection": "keep-alive",
        "Referer": "https://xxcapp.xidian.edu.cn/ncov/wap/default/index",
        "Cookie": login_cookies
    }
    resp = requests.post(
        url=url,
        headers=headers,
        data=load_data
    );

    # WXPUSHER通知
    sendmsg_url0="http://wxpusher.zjiecode.com/api/send/message/?appToken="+WXPUSHER_appToken+"&content="
    sendmsg_url2="&uid="+WXPUSHER_uid
    retstr = resp.text
    #print (retstr)
    if "您已上报过" in retstr:
        print("今日已完成填报\n")
        sendmsg_url=sendmsg_url0+"已填报"+sendmsg_url2
        sendmsg_recall=requests.get(url=sendmsg_url)
        #print(sendmsg_recall)
    elif "操作成功" in retstr:
        print("填报成功，随后进行确认！\n")
        sendmsg_url=sendmsg_url0+"填报成功"+sendmsg_url2
        sendmsg_recall=requests.get(url=sendmsg_url)
        #print(sendmsg_recall)
    else:
        print("填报失败！！!\n")
        sendmsg_url=sendmsg_url0+"填报失败！！！"+sendmsg_url2
        sendmsg_recall=requests.get(url=sendmsg_url)
        #print(sendmsg_recall)

#main();
def main_handler(event, context):
    main();

