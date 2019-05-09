#!/usr/bin/python3
#-*- coding: UTF-8 -*- 
#@Author:
#@Time:
#@File:dd_robot.py

import json
import requests
from alarmrest.logs import LogtoLog

logging = LogtoLog().getlog()

token = "3e3905aa474ce33187ddc5abf28ecb747eb02bf7bdea44b98e2dda606dd3189e"

def dingtalk_robot(content):
    contentlist = content.split()
    alarm_name = contentlist[6].split(':')[1]
    hostname = contentlist[2].split(':')[1]
    alarm_level = contentlist[1]
    alarm_metric = contentlist[3].split(':')[1]
    alarm_value = contentlist[5].split(':')[1]
    alarm_time = contentlist[8].split('Timestamp:')[1]
    alarm_tags = contentlist[4].split(':')[1]
    alarm_status = contentlist[0].split('=')[1]
    titlename = hostname + '--' + alarm_name + '--' + alarm_level
    datas = {
     "msgtype": "markdown",
     "markdown": {
         "title": titlename,
         "text": "###救火英雄：%s  \n" % titlename +
                "> 告警名称：" + alarm_name + "\n\n" +
                "> 告警主机：" + hostname + "\n\n" +
                "> 告警等级：" + alarm_level + "\n\n" +
                "> 告警指标：" + alarm_metric + "\n\n" +
                "> 告警阀值：" + alarm_value + "\n\n" +
                "> 告警时间：" + alarm_time + "\n\n" +
                "> 告警标签：" + alarm_tags + "\n\n" +
                "> 告警状态：" + alarm_status
     },
    "at": {
        "isAtAll": True
    }
 }
    try:
        headers = {'Content-type': 'application/json'}
        requests.post("https://oapi.dingtalk.com/robot/send?access_token=%s" % token, data=json.dumps(datas), headers=headers)
    except Exception as err:
        logging.warning("http url not connection, %s" % err)

