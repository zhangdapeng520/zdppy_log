from .loguru import logger
import sys

config = {
    "format": "{time:YYYY-MM-DD HH:mm:ss} | {level} | {file}:{line} | {message}",
    "level": "INFO",
    "rotation": "100 MB",
    "compression": "zip",
    "enqueue": True,
    "encoding": "utf-8",
    "serialize": True,
    "retention": 10,
}


class Log:
    """
    日志对象
    """

    def __init__(self, log_file_path: str = "log.log",
                 level: str = "INFO",
                 rotation: str = "100 MB",
                 serialize: bool = False,
                 full_path: bool = False,
                 retention: int = 10,
                 debug: bool = True,
                 is_only_console: bool = False,
                 ):
        """
        创建日志对象
        :param level 日志等级
        :param rotation 单个日志文件大小
        :param serialize 是否开启格式化日志
        :param full_path 是否启用全路径。默认关闭，开启后日志路径的模块路径显示为完整绝对路径。
        :param retention 日志文件备份个数
        :param debug 是否为开发环境
        :param is_only_console 是否只输出到控制台
        """
        # 初始化日志
        logger.remove()

        # 日志等级
        self.level = level.upper()
        config["level"] = level.upper()

        # 日志大小
        self.rotation = rotation
        config["rotation"] = rotation

        # 是否json化
        self.serialize = serialize
        config["serialize"] = serialize

        # 日志个数
        self.retention = retention
        config["retention"] = retention

        # 日志格式
        self.format = format

        # 是否为全路径
        self.full_path = full_path

        # 是否为debug模式
        self.__debug = debug

        # 是否只输出到控制台
        self.__is_only_console = is_only_console

        if is_only_console:
            # 创建控制台日志
            if self.__debug:
                # logger.add(sys.stderr, level="DEBUG", format=format)
                logger.add(sys.stderr, level="DEBUG")
            else:
                logger.add(sys.stderr, level=level.upper())
            self.__set_logger_method(logger)
        else:
            # 创建文件日志
            # 颜色说明：green 绿色 level 等级颜色 cyan 天蓝色
            # config["format"] = format
            logger.add(log_file_path, **config)

            # 创建控制台日志
            if self.__debug:
                # logger.add(sys.stderr, level="DEBUG", format=format)
                logger.add(sys.stderr, level="DEBUG")
            self.__set_logger_method(logger)
        # 捕获错误
        self.catch = logger.catch

    def __set_logger_method(self, logger):
        """
        设置日志方法
        """
        # 日志方法
        self.debug = logger.debug
        self.info = logger.info
        self.success = logger.success
        self.warning = logger.warning
        self.error = logger.error
        self.critical = logger.critical
