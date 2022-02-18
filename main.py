from zdppy_log import Log

log1 = Log("logs/zdppy/zdppy_log1.log")


@log1.catch()
def my_function(x, y, z):
    # An error? It's caught anyway!
    return 1 / (x + y + z)


my_function(0, 0, 0)
# logger.add("out.log", backtrace=True, diagnose=True)  # Caution, may leak sensitive data in prod

log2 = Log("logs/zdppy/zdppy_log2.log")
log2.debug("log2日志")
log2.info("log2日志")
log2.warning("log2日志")
log2.error("log2日志")
log2.critical("log2日志")

log3 = Log("logs/zdppy/zdppy_log3.log")
log3.debug("log3日志")
log3.info("log3日志")
log3.warning("log3日志")
log3.error("log3日志")
log3.critical("log3日志")


