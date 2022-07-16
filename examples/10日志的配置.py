# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :  10日志的配置.py
@Time    :  2022/7/16 8:31
@Author  :  张大鹏
@Version :  v0.1.0
@Contact :  lxgzhw@163.com
@License :  (C)Copyright 2022-2023
@Desc    :  描述
"""
from zdppy_log import logger

logger.add("runtime_{time}.log")  # 创建了一个文件名为runtime的log文件

# 通过配置rotation参数，指定日志文件滚动记录的条件，如下所示：
# 通过这样的配置我们就可以实现每 500MB 存储一个文件，每个 log 文件过大就会新创建一个新的 log 文件。
logger.add("file_1.log", rotation="500 MB")  # Automatically rotate too big file

# 我们可以在创建文件的时候加一个(time)占位符，这样在生成时可以自动将时间替换进去，生成一个文件名包含时间的 log 文件。
# 通过下面的配置，可以实现没天中午12：00创建一个log文件输出了。
logger.add("file_2.log", rotation="12:00")  # New file is created each day at noon

# 通过下面的配置可以实现每隔1周创建一个新的log文件输出了。
logger.add("file_3.log", rotation="1 week")  # Once the file is too old, it's rotated

# 通过配置retention参数，可以指定日志的保留时长：
# 通过下面的配置，就可以指定日志最多保留10天，每隔10天之后就会清理旧的日志，这样就不会造成内存浪费。
logger.add("file_X.log", retention="10 days")  # Cleanup after some time

# 通过配置compression参数可以指定日志文件的压缩格式：
logger.add("file_Y.log", compression="zip")  # Save some loved space
logger.debug("This's a log message in file")
