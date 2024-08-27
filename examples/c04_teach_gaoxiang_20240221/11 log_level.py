import sys

from log import logger

logger.debug("debug...")
logger.info("info...")
logger.success("success...")
logger.warning("warning...")
logger.error("error...")

logger.debug("设置日志级别为info")
logger.remove()
logger.add(sys.stdout, level="INFO")

logger.debug("debug...")
logger.info("info...")
logger.success("success...")
logger.warning("warning...")
logger.error("error...")
