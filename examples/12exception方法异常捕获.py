# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :  12exception方法异常捕获.py
@Time    :  2022/7/16 8:35
@Author  :  张大鹏
@Version :  v0.1.0
@Contact :  lxgzhw@163.com
@License :  (C)Copyright 2022-2023
@Desc    :  描述
"""
from zdppy_log import logger

logger.add("runtime.log")


def my_function1(x, y, z):
    try:
        return 1 / (x + y + z)
    except ZeroDivisionError:
        logger.exception("What?!")


my_function1(0, 0, 0)
