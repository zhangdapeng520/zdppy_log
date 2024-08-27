from log import logger

# logger.add("zdppy_log_{time}.log")  # 创建了一个文件名为runtime的log文件

logger.debug("This's a log message in file", a=1, b=True)
