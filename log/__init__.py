from .logger import logger
from . import level

# 添加设置日志级别的方法
setattr(logger, "set_debug", level.set_debug)
setattr(logger, "set_info", level.set_info)
setattr(logger, "set_error", level.set_error)
setattr(logger, "set_success", level.set_success)
setattr(logger, "set_warning", level.set_warning)
setattr(logger, "set_error", level.set_error)

__all__ = ["logger"]
