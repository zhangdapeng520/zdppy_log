from zdppy_log import logger


def init():
    init_logger()
    logger.debug("debug22222")


def init_logger():
    logger.add("../tmp/logs/zdppy_log.zdppy_log")
    logger.debug("debug111")
