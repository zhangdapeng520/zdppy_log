from loguru import logger
import sys

config = {
    "format": "{time:YYYY-MM-DD at HH:mm:ss} | {level} | {file}:{line} | {message}",
    "level": "INFO",
    "rotation": "100 MB",
    "compression": "zip",
    "enqueue": True,
    "encoding": "utf-8",
    "serialize": True,
    "retention": 10,
}
logger.add(sys.stderr, level="DEBUG")
