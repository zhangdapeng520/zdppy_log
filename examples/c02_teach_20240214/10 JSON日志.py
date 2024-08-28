from zdppy_log import logger

logger.add("zdppy_log-{time}.zdppy_log", serialize=True)  # 指定日志文件
logger.debug("日志", a=1, b=1.1, c=True, d="")
logger.info("日志", a=1, b=1.1, c=True, d="")
logger.warning("日志", a=1, b=1.1, c=True, d="")
logger.error("日志", a=1, b=1.1, c=True, d="")
