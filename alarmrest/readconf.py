#!/usr/bin/python3
#-*- coding: UTF-8 -*- 
#@Author:

import json
from alarmrest.logs import *

CONFNAME = r"/app/ddingalarm/conf/cfg.json"

#读取配置文件，并以字典形式返回
def read_cof():
    log = LogtoLog().getlog()
    '''
    读取配置文件cfg.json
    :return: 返回json数据cnfdata
    '''
    try:
        ofs = open(CONFNAME, encoding='utf-8')
    except IOError as err:
        log.error("文件不存在，或者权限不足!!! " + str(err))
    cnfdata = json.load(ofs)
    return cnfdata
