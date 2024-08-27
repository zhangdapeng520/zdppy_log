import sys

from log import logger

logger.open_level_file()
logger.debug("debug...")
logger.info("info...")
logger.success("success...")
logger.warning("warning...")
logger.error("error...")

logger.open_level_file(is_time=True)
logger.debug("debug...")
logger.info("info...")
logger.success("success...")
logger.warning("warning...")
logger.error("error...")
