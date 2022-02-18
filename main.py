from zdppy_log import logger, config

config["rotation"] = "1 MB"
config["retention"] = 1

logger.add("logs/zdppy/zdppy_log.log", **config)

for i in range(100000):
    logger.debug("debug日志")
    logger.info("info日志")
    logger.warning("warning日志")
    logger.error("error日志")


@logger.catch
def my_function(x, y, z):
    # An error? It's caught anyway!
    return 1 / (x + y + z)


my_function(0, 0, 0)
# logger.add("out.log", backtrace=True, diagnose=True)  # Caution, may leak sensitive data in prod
