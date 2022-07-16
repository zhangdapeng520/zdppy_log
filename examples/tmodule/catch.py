# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :  catch.py
@Time    :  2022/7/16 8:36
@Author  :  张大鹏
@Version :  v0.1.0
@Contact :  lxgzhw@163.com
@License :  (C)Copyright 2022-2023
@Desc    :  描述
"""
from zdppy_log import logger


def func(a, b):
    logger.info("Process func")
    return a / b


def nested(c):
    try:
        func(5, c)
    except ZeroDivisionError:
        logger.exception("What?!")
