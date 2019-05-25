#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Author:

import os
import sys
from alarmrest.readconf import *
from alarmrest.logs import *


def usage():
    print('''''')


log = LogtoLog().getlog()


def stop(listenport):
    """
    停止服务，直接kill进程
    """
    os.system("ps aux|grep %s|grep -v grep|awk -F ' ' '{print $2}'|xargs kill -9" % (listenport,))
    log.info("Service stoped successfully！！！")


def start(listenip, listenport):
    """
    获取配置文件参数得到监听得地址和端口，启动service
    """
    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0)
    except OSError as err:
        logging.info(sys.stderr, "fork #1 failed: %d (%s)" % (err.errno, err.strerror))
        sys.exit(1)
    os.chdir("/")
    os.setsid()
    os.umask(0)
    try:
        pid = os.fork()
        if pid > 0:
            logging.info("Service started successfully，Daemon PID %d" % pid)
            sys.exit(0)
    except OSError as err:
        logging.info(sys.stderr, "fork #2 failed: %d (%s)" % (err.errno, err.strerror))
        sys.exit(1)
    os.system('python3 manage.py runserver %s:%s' % (listenip, listenport))


def restart(listenip, listenport):
    """
    停止服务，直接kill进程,然后重启服务
    """
    stop(listenport)
    start(listenip, listenport)
    log.info("Service restarted successfully！！！")


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
