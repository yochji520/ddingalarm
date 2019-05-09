#!/usr/bin/python3
#-*- coding: UTF-8 -*-
#@Author:

import os
import sys
from alarmrest.readconf import *
from alarmrest.logs import *

#帮助信息
def usage():
    print('''''')

log = LogtoLog().getlog()
def stop(listenport):
    '''
    停止服务，直接kill进程
    '''
    os.system("ps aux|grep %s|grep -v grep|awk -F ' ' '{print $2}'|xargs kill -9" % (listenport,))
    log.info("服务已经停止！！！")

def start(listenip, listenport):
    '''
    获取配置文件参数得到监听得地址和端口，启动service
    '''
    os.system('python3 manage.py runserver %s:%s' % (listenip, listenport))
    log.info("服务启动成功！！！")

def restart(listenip, listenport):
    '''
    停止服务，直接kill进程,然后重启服务
    '''
    stop(listenport)
    start(listenip, listenport)
    log.info("服务已经重启！！！")

if __name__ == "__main__":
    conf = read_cof()
    listen = conf['http']['listen']
    listenip = listen[:7]
    listenport = listen[8:]
    args = sys.argv[1]
    if args == 'start':
        start(listenip, listenport)
    elif args == 'stop':
        stop(listenport)
    elif args == 'restart':
        restart(listenip, listenport)
    else:
        pass