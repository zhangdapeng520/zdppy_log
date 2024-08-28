from zdppy_log import logger

logger.add("a/b/c/log1.zdppy_log")  # 指定日志文件
logger.add("aa/bb/cc/log2.zdppy_log")  # 指定日志文件
logger.debug("日志", a=1, b=1.1, c=True, d="")
logger.info("日志", a=1, b=1.1, c=True, d="")
logger.warning("日志", a=1, b=1.1, c=True, d="")
logger.error("日志", a=1, b=1.1, c=True, d="")
