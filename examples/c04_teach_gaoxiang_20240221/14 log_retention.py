from zdppy_log import logger

logger.add("tmp/logs/zdppy_log.zdppy_log", rotation="1KB", retention=3)
for _ in range(1000):
    logger.debug("debug..." * 100)
