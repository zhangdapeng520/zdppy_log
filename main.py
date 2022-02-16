from zdppy_log import logger

for i in range(100000):
    logger.info("No matter added sinks, this message is not displayed")
    logger.enable("my_library")
    logger.info("This message however is propagated to the sinks")


@logger.catch
def my_function(x, y, z):
    # An error? It's caught anyway!
    return 1 / (x + y + z)


my_function(0, 0, 0)
# logger.add("out.log", backtrace=True, diagnose=True)  # Caution, may leak sensitive data in prod
