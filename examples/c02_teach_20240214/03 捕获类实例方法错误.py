from log import logger


class A:
    @logger.catch()
    def f(self, a, b):
        return a / b


if __name__ == '__main__':
    a = A()
    a.f(1, 1)
    a.f(1, 0)  # 报错
    print("这个代码会执行吗？")
