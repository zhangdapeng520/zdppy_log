import sys
from .logger import logger


def set_level(out=sys.stdout, level="DEBUG"):
    """设置日志级别"""
    logger.remove()
    logger.add(out, level=level)


def set_debug():
    """设置DEBUG级别"""
    return set_level()


def set_info(out=sys.stdout):
    """设置INFO级别"""
    return set_level(out, "INFO")


def set_success(out=sys.stdout):
    return set_level(out, "SUCCESS")


def set_warning(out=sys.stderr):
    """设置SUCCESS级别"""
    return set_level(out, "WARNING")


def set_error(out=sys.stderr):
    """设置ERROR级别"""
    return set_level(out, "ERROR")
