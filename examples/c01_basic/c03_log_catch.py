from log import logger


@logger.catch
def f1():
    raise Exception("f1")


@logger.catch
def f2():
    f1()
    raise Exception("f2")


f2()
