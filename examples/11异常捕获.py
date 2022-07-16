# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :  11异常捕获.py
@Time    :  2022/7/16 8:34
@Author  :  张大鹏
@Version :  v0.1.0
@Contact :  lxgzhw@163.com
@License :  (C)Copyright 2022-2023
@Desc    :  描述
"""
from zdppy_log import logger

logger.add("runtime.log")


@logger.catch
def my_function(x, y, z):
    return 1 / (x + y + z)  # An error? It's caught anyway!


my_function(0, 0, 0)
