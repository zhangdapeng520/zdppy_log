from zdppy_log import Log

log1 = Log("logs/zdppy/zdppy_log1.log")


@log1.catch()
def my_function(x, y, z):
    return 1 / (x + y + z)


my_function(0, 0, 0)
