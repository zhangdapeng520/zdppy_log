from zdppy_log import logger

logger.add("zdppy_log_{time}.zdppy_log", serialize=True)
logger.debug("log1 debug", a=1, b=2, c=33.33)
logger.info("log1 info", 1, 2, 3, 4)
logger.warning("log1 warning")
logger.error("log1 error")
logger.critical("log1 critical")
