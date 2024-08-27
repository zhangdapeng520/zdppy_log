import sys
from log import logger

# 删去import logger之后自动产生的handler，不删除的话会出现重复输出的现象
logger.remove()

# 添加一个可以修改控制的handler
# 支持的级别有： DEBUG INFO SUCCESS WARNING ERROR CRITICAL
logger.add(sys.stderr, level="INFO")

# 输出日志
logger.debug("debug...")
logger.info("info...")
logger.success("success...")
logger.warning("warning...")
logger.error("error...")
logger.critical("critical...")
