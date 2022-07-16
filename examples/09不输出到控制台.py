# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :  09不输出到控制台.py
@Time    :  2022/7/16 8:30
@Author  :  张大鹏
@Version :  v0.1.0
@Contact :  lxgzhw@163.com
@License :  (C)Copyright 2022-2023
@Desc    :  描述
"""
from zdppy_log import logger

logger.remove(handler_id=None)

logger.add("runtime.log")  # 创建了一个文件名为runtime的log文件

logger.debug("This's a log message in file")
