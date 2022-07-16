# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :  13多模块使用.py
@Time    :  2022/7/16 8:36
@Author  :  张大鹏
@Version :  v0.1.0
@Contact :  lxgzhw@163.com
@License :  (C)Copyright 2022-2023
@Desc    :  描述
"""
# coding:utf-8

from zdppy_log import logger

import tmodule.catch as ec3

if __name__ == '__main__':
    logger.add("run.log")

    logger.info("Start!")

    ec3.nested(0)

    logger.info("End!")
