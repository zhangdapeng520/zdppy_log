from zdppy_log import Log

# 记录所有级别的日志到控制台
log1 = Log(debug=True, is_only_console=True)
log1.debug("log1 debug")
log1.info("log1 info")
log1.warning("log1 warning")
log1.error("log1 error")
log1.critical("log1 critical")

# 记录info以上级别的日志到控制台
log2 = Log(debug=False, is_only_console=True)
log2.debug("log2 debug")
log2.info("log2 info")
log2.warning("log2 warning")
log2.error("log2 error")
log2.critical("log2 critical")

# 记录error以上级别的日志到控制台
log3 = Log(debug=False, level="ERROR", is_only_console=True)
log3.debug("log3 debug")
log3.info("log3 info")
log3.warning("log3 warning")
log3.error("log3 error")
log3.critical("log3 critical")
