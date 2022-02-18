from loguru import logger
import sys

config = {
    "format": "{time:YYYY-MM-DD at HH:mm:ss} | {level} | {file}:{line} | {message}",
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

    def __init__(self, log_file_path: str = "logs/zdppy/zdppy_log.log",
                 level: str = "INFO",
                 rotation: str = "100 MB",
                 serialize: bool = True,
                 retention: int = 10
                 ):
        # 初始化日志
        logger.remove()

        # 日志等级
        self.level = level
        config["level"] = level

        # 日志大小
        self.rotation = rotation
        config["rotation"] = rotation

        # 是否json化
        self.serialize = serialize
        config["serialize"] = serialize

        # 日志个数
        self.retention = retention
        config["retention"] = retention

        # 创建日志
        logger.add(log_file_path, **config)
        logger.add(sys.stderr, level="DEBUG")
        self.log = logger

    def catch(self):
        """
        捕获日志
        :return:
        """
        return self.log.catch()

    def debug(self, *args, **kwargs):
        return self.log.debug(*args, **kwargs)

    def info(self, *args, **kwargs):
        return self.log.info(*args, **kwargs)

    def warning(self, *args, **kwargs):
        return self.log.warning(*args, **kwargs)

    def error(self, *args, **kwargs):
        return self.log.error(*args, **kwargs)

    def critical(self, *args, **kwargs):
        return self.log.critical(*args, **kwargs)
