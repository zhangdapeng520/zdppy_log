from log import logger


@logger.catch()
def f(a, b):
    return a / b


if __name__ == '__main__':
    f(1, 1)
    f(1, 0)  # 报错
    print("这个代码会执行吗？")
