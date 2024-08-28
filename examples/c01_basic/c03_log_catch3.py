from zdppy_log import logger


@logger.catch(level='ERROR')
def f1():
    raise Exception("f1")


@logger.catch
def f2():
    f1()


f2()
