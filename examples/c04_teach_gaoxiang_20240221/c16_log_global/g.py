from log import logger


def init():
    init_logger()
    logger.debug("debug22222")


def init_logger():
    logger.add("../tmp/logs/log.log")
    logger.debug("debug111")
