from zdppy_log import logger

# logger.add("zdppy_log_{time}.zdppy_log")  # 创建了一个文件名为runtime的log文件

logger.debug("This's a zdppy_log message in file", a=1, b=True)
