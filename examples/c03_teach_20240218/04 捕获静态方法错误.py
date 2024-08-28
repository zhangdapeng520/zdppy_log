from zdppy_log import logger


class A:
    @logger.catch()
    @staticmethod
    def f(a, b):
        return a / b


if __name__ == '__main__':
    A.f(1, 1)
    A.f(1, 0)  # 报错
    print("这个代码会执行吗？")
