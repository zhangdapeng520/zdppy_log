import sys

from log import logger

logger.debug("debug...")
logger.info("info...")
logger.success("success...")
logger.warning("warning...")
logger.error("error...")

logger.debug("设置日志级别为info")
# 这里设置日志级别的方法有： set_debug set_info set_success set_warning set_error
logger.set_debug()
logger.add("tmp/info.log", level="INFO", filter=lambda x: "INFO" in str(x["level"]).upper())
logger.add("tmp/error.log", level="INFO", filter=lambda x: "ERROR" in str(x["level"]).upper())

logger.debug("debug...")
logger.info("info...")
logger.success("success...")
logger.warning("warning...")
logger.error("error...")
