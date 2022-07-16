# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :  07add函数.py
@Time    :  2022/7/16 8:28
@Author  :  张大鹏
@Version :  v0.1.0
@Contact :  lxgzhw@163.com
@License :  (C)Copyright 2022-2023
@Desc    :  描述
"""
import sys
from zdppy_log import logger

logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level="INFO")

logger.debug("This's a new log message")
