# -*- coding: utf-8 -*-

"""
封装log方法
"""

import logging
import os
import time
import stat
import datetime
from hashlib import md5
from colorama import Fore, Style

TRACE_ID_LIST = []
LEVELS = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'error': logging.ERROR,
    'critical': logging.CRITICAL
}

logger = logging.getLogger()
level = 'default'


def set_file_permission(filename):
    # 设置日志目录文件及权限
    path = filename[0:filename.rfind('/')]
    if not os.path.isdir(path):
        os.makedirs(path)
    if not os.path.isfile(filename):
        return None
    try:
        # 赋予文件777的权限,防止不同用户访问时报错
        os.chmod(filename, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
        return True
    except Exception as e:
        print('设置日志文件权限错误，error：{}'.format(e))
        return False


def set_handler(levels):
    # 日志文件内写入内容
    if levels == 'error':
        set_file_permission(MyLog.err_file)
        logger.addHandler(MyLog.err_handler)
    set_file_permission(MyLog.log_file)
    logger.addHandler(MyLog.handler)


def remove_handler(levels):
    if levels == 'error':
        logger.removeHandler(MyLog.err_handler)
    logger.removeHandler(MyLog.handler)


def get_current_time():
    return datetime.datetime.now().strftime(MyLog.date)


class MyLog:
    backup_count = 5
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    local_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    log_file = path + '/Log/info.log'
    err_file = path + '/Log/error.log'
    logger.setLevel(LEVELS.get(level, logging.NOTSET))

    date = '%Y-%m-%d %H:%M:%S.%f'

    from logging.handlers import TimedRotatingFileHandler
    # 分割日志记录
    handler = TimedRotatingFileHandler(filename=log_file, when="MIDNIGHT", interval=1, backupCount=backup_count,
                                       encoding='utf-8')
    err_handler = TimedRotatingFileHandler(filename=err_file, when="MIDNIGHT", interval=1, backupCount=backup_count,
                                           encoding='utf-8')

    @staticmethod
    def debug(log_meg):
        set_handler('debug')
        logger.debug("[DEBUG " + get_current_time() + "]" + str(log_meg))
        print(Fore.LIGHTGREEN_EX + "[DEBUG]" + str(log_meg) + Style.RESET_ALL)
        remove_handler('debug')

    @staticmethod
    def info(log_meg):
        set_handler('info')
        logger.info("[INFO " + get_current_time() + "]" + str(log_meg))
        print("[INFO]" + str(log_meg))
        remove_handler('info')

    @staticmethod
    def warning(log_meg):
        set_handler('warning')
        logger.warning("[WARNING " + get_current_time() + "]" + str(log_meg))
        print(Fore.LIGHTYELLOW_EX + "[WARNING]" + str(log_meg) + Style.RESET_ALL)
        remove_handler('warning')

    @staticmethod
    def error(log_meg):
        try:
            raise RuntimeError
        except RuntimeError:
            import sys
            f = sys.exc_info()[2].tb_frame.f_back
        datas = 'The error source: ' + f.f_code.co_filename + ' ' + f.f_code.co_name + ' ' + str(f.f_lineno)
        set_handler('error')
        logger.error("[ERROR " + get_current_time() + "]" + str(log_meg), exc_info=True)
        logger.error(datas)
        print(Fore.LIGHTRED_EX + "[ERROR]" + str(log_meg) + Style.RESET_ALL)
        print(datas)
        remove_handler('error')

    @staticmethod
    def critical(log_meg):
        set_handler('critical')
        logger.critical("[CRITICAL " + get_current_time() + "]" + str(log_meg))
        print(Fore.RED + "[CRITICAL]" + str(log_meg) + Style.RESET_ALL)
        remove_handler('critical')
