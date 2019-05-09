#!/usr/bin/python3
#-*- coding: UTF-8 -*-
import time
import logging

class LogtoLog(object):
    def __init__(self, logger=None):
        '''指定保存日志的文件路径，日志级别，以及调用文件将日志存入到指定的文件中'''
        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.INFO)
        # 创建一个handler，用于写入日志文件
        self.log_time = time.strftime("%Y_%m_%d_")
        self.log_path = "/app/ddingalarm/log/"
        self.log_name = self.log_path + self.log_time + 'running.log'

        fh = logging.FileHandler(self.log_name, 'a', encoding='utf-8')
        fh.setLevel(logging.INFO)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter('[%(asctime)s] %(filename)s-->%(funcName)s line:%(lineno)d [%(levelname)s]%(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

        # 关闭打开的文件
        fh.close()
        ch.close()

    def getlog(self):
        return self.logger
