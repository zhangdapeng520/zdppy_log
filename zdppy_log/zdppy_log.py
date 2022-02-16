from loguru import logger
import sys

logger.add("logs/zdppy/zdppy_log.log", format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}", level="INFO",
           rotation="100 MB", compression="zip", enqueue=True)
logger.add(sys.stderr, level="DEBUG")
