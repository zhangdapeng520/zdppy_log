from zdppy_log import Log

log1 = Log("log.log")

log2 = Log("log2.log")

# 格式1：自动填充参数
log2.debug("log2日志", 1, "a", 2.2, True)

# 格式2：手动填充参数
log2.info("log2日志 a={} b={} c={} d={}", 1, "a", 2.2, True)

# 格式3：字典参数
log2.warning("log2日志", a=1, b="a", c=2.2, d=True)

log2.error("log2日志", 1, "a", 2.2, True)
log2.critical("log2日志", 1, "a", 2.2, True)

log3 = Log("log3.log", debug=False)
log3.debug("log3日志", 1, "a", 2.2, True)
log3.info("log3日志", 1, "a", 2.2, True)
log3.warning("log3日志", 1, "a", 2.2, True)
log3.error("log3日志", 1, "a", 2.2, True)
log3.critical("log3日志", 1, "a", 2.2, True)
