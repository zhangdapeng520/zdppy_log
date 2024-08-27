import sys
from log import logger

# 删去import logger之后自动产生的handler，不删除的话会出现重复输出的现象
logger.remove()

# 添加一个可以修改控制的handler
# 支持的级别有： DEBUG INFO SUCCESS WARNING ERROR CRITICAL
# 日志切割： KB MB GB
logger.add(sys.stdout, level="DEBUG")
logger.add("tmp/{time}.log", level="DEBUG", rotation="200KB")

# 输出日志
for i in range(1000):
    logger.debug("debug...")
    logger.info("info...")
    logger.success("success...")
    logger.warning("warning...")
    logger.error("error...")
    logger.critical("critical...")
