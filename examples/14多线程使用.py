# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :  14多线程使用.py
@Time    :  2022/7/16 8:37
@Author  :  张大鹏
@Version :  v0.1.0
@Contact :  lxgzhw@163.com
@License :  (C)Copyright 2022-2023
@Desc    :  描述
"""
# coding:utf-8

from atexit import register
from random import randrange
from threading import Thread, Lock, current_thread
from time import sleep, ctime

from zdppy_log import logger


class CleanOutputSet(set):
    def __str__(self):
        return ','.join(x for x in self)


lock = Lock()
loops = (randrange(2, 5) for x in range(randrange(3, 7)))
remaining = CleanOutputSet()


def loop(nsec):
    myname = current_thread().name

    logger.info("Startted {}", myname)

    '''
    锁的申请和释放交给with上下文管理器
    '''
    with lock:
        remaining.add(myname)
    sleep(nsec)

    logger.info("Completed {} ({} secs)", myname, nsec)

    with lock:
        remaining.remove(myname)
        logger.info("Remaining:{}", (remaining or 'NONE'))


'''
_main()函数是一个特殊的函数，只有这个模块从命令行直接运行时才会执行该函数（不能被其他模块导入）
'''


def _main():
    for pause in loops:
        Thread(target=loop, args=(pause,)).start()


'''
这个函数（装饰器的方式）会在python解释器中注册一个退出函数，也就是说，他会在脚本退出之前请求调用这个特殊函数
'''


@register
def _atexit():
    logger.info("All Thread DONE!")
    logger.info("\n===========================================================================\n")


if __name__ == '__main__':
    logger.add("run.log")

    _main()
