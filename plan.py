# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 13:32:02 2018

@author: ren
"""
import operator
import requests
from  senMail import mail
import time

def RequestWeb(url,head):#请求网页函数
    # 向携程发送post请求
    r = requests.post(url, head)
    # 对获取到的机票信息进行排序，返回一个列表
    #sorted_x = sorted(r.json()["data"]["oneWayPrice"][0].items(), key=operator.itemgetter(1))
    # 方式一，去除最小的前三个数，如果哪个日期存在里面的就给我发送消息
    # i = 0
    # while i <= 3:
    #    print(sorted_x[i])
    #    i += 1
    # 方式二，当价格低于某一价格时通知我
    # 低于价格的时候给我发消息

    date = '20190112'#获取价格
    print("当前的价格是：", r.json()["data"]["oneWayPrice"][0][date])

    i=0
    while i<3:
        if r.json()["data"]["oneWayPrice"][0][date] < 600:
            message_send = '机票日期为：'+date+'当前价格为：'+str(r.json()["data"]["oneWayPrice"][0][date])+'长春-贵阳'
            ret = mail(message_send)
            if ret:
                print("邮件发送成功")
            else:
                print("邮件发送失败")
        i=i+1

#请求参数


if __name__=="__main__":
    url = "https://flights.ctrip.com/itinerary/api/12808/lowestPrice"
    head = {"flightWay": "Oneway", "dcity": "CGQ", "acity": "KWE"}
    while(1):
        RequestWeb(url,head)
        time.sleep(1800)

# str = input("请输入：");#输入要走的日期等
# print(type(str))
# print("输入的符号是：",str)
