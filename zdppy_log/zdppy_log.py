from loguru import logger
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

    def __init__(self, log_file_path: str = "logs/zdppy/zdppy_log.log",
                 level: str = "INFO",
                 format:str = "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | <cyan>{extra[module_name]}</cyan>:<cyan>{extra[func_name]}</cyan>:<cyan>{extra[line_no]}</cyan> | <level>{message}</level>",
                 rotation: str = "100 MB",
                 serialize: bool = False,
                 retention: int = 10,
                 debug: bool = True
                 ):
        """
        创建日志对象
        """
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

        # 日志格式
        self.format = format

        # 是否为debug模式
        self.__debug = debug

        # 创建文件日志
        # 颜色说明：green 绿色 level 等级颜色 cyan 天蓝色
        config["format"] = format
        logger.add(log_file_path, **config)

        # 创建控制台日志
        if self.__debug:
            logger.add(sys.stderr, level="DEBUG", format=format)
        self.log = logger

    def catch(self):
        """
        捕获日志
        :return:
        """
        return self.log.catch()

    def __get_log_where(self):
        """
        获取日志的路径信息
        """
        result = {}  # 存储信息

        # 获取被调用函数所在模块文件名
        module_name = sys._getframe(1).f_code.co_filename
        result["module_name"] = module_name

        # 获取被调用函数名称
        func_name = sys._getframe(1).f_code.co_name
        result["func_name"] = func_name

        # 获取被调用函数在被调用时所处代码行数
        line_no = sys._getframe(1).f_lineno
        result["line_no"] = line_no

        # 返回结果
        return result

    def debug(self, *args, **kwargs):
        """
        记录DEBUG级别的日志
        """
        info = self.__get_log_where()
        extra_logger = self.log.bind(**info)
        return extra_logger.debug(*args, **kwargs)

    def info(self, *args, **kwargs):
        """
        记录INFO级别的日志
        """
        info = self.__get_log_where()
        extra_logger = self.log.bind(**info)
        return extra_logger.info(*args, **kwargs)

    def success(self, *args, **kwargs):
        """
        记录SUCCESS级别的日志
        """
        info = self.__get_log_where()
        extra_logger = self.log.bind(**info)
        return extra_logger.success(*args, **kwargs)

    def warning(self, *args, **kwargs):
        """
        记录WARNING级别的日志
        """
        info = self.__get_log_where()
        extra_logger = self.log.bind(**info)
        return extra_logger.warning(*args, **kwargs)

    def error(self, *args, **kwargs):
        """
        记录ERROR级别的日志
        """
        info = self.__get_log_where()
        extra_logger = self.log.bind(**info)
        return extra_logger.error(*args, **kwargs)

    def critical(self, *args, **kwargs):
        """
        记录CRITICAL级别的日志
        """
        info = self.__get_log_where()
        extra_logger = self.log.bind(**info)
        return extra_logger.critical(*args, **kwargs)
