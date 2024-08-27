# zdppy_log

python的日志库

项目地址：https://github.com/zhangdapeng520/zdppy_log

## 版本历史

- v0.1.9 新增：自动记录动态参数和字典参数

## 安装方式

```shell script
pip install log
```

## 使用方式

```python
from log import Log

log1 = Log("logs/zdppy/zdppy_log1.log")


@log1.catch()
def my_function(x, y, z):
    # An error? It's caught anyway!
    return 1 / (x + y + z)


my_function(0, 0, 0)
# logger.add("out.log", backtrace=True, diagnose=True)  # Caution, may leak sensitive data in prod

log2 = Log("logs/zdppy/zdppy_log2.log")
log2.debug("log2日志")
log2.info("log2日志")
log2.warning("log2日志")
log2.error("log2日志")
log2.critical("log2日志")

log3 = Log("logs/zdppy/zdppy_log3.log", debug=False)
log3.debug("log3日志")
log3.info("log3日志")
log3.warning("log3日志")
log3.error("log3日志")
log3.critical("log3日志")
```

## 版本历史

- v0.1.2 2022/2/19 增加debug模式；默认json日志为False
- v0.1.3 2022/3/4 增加记录日志文件，日志方法，日志行数的功能
- v0.1.4 2022/3/5 移除第三方依赖
- v0.1.5 2022/3/5 增加控制是否开启日志全路径的开关量
- v0.1.6 2022/3/16 增加只输出到控制台的开关量及底层代码优化
- v0.1.7 2022/3/16 BUG修复及完善使用文档
- v0.1.8 2022/5/17 优化：底层代码结构优化

## 使用案例

### 案例1：基本使用

```python
from log import Log

log1 = Log("logs/zdppy/zdppy_log1.log")

log2 = Log("logs/zdppy/zdppy_log2.log")
log2.debug("log2日志")
log2.info("log2日志")
log2.warning("log2日志")
log2.error("log2日志")
log2.critical("log2日志")

log3 = Log("logs/zdppy/zdppy_log3.log", debug=False)
log3.debug("log3日志")
log3.info("log3日志")
log3.warning("log3日志")
log3.error("log3日志")
log3.critical("log3日志")
```

### 案例2：捕获方法错误

```python
from log import Log

log1 = Log("logs/zdppy/zdppy_log1.log")


@log1.catch()
def my_function(x, y, z):
    return 1 / (x + y + z)


my_function(0, 0, 0)
```

### 案例3：只往控制台输出

```python
from log import Log

# 记录所有级别的日志到控制台
log1 = Log(debug=True, is_only_console=True)
log1.debug("log1 debug")
log1.info("log1 info")
log1.warning("log1 warning")
log1.error("log1 error")
log1.critical("log1 critical")

# 记录info以上级别的日志到控制台
log2 = Log(debug=False, is_only_console=True)
log2.debug("log2 debug")
log2.info("log2 info")
log2.warning("log2 warning")
log2.error("log2 error")
log2.critical("log2 critical")

# 记录error以上级别的日志到控制台
log3 = Log(debug=False, level="ERROR", is_only_console=True)
log3.debug("log3 debug")
log3.info("log3 info")
log3.warning("log3 warning")
log3.error("log3 error")
log3.critical("log3 critical")
```

### 案例4：同时输出到控制台和日志文件

```python
from log import Log

# 记录info级别的日志，并将所有级别日志输出到控制台
log1 = Log(debug=True)
log1.debug("log1 debug")
log1.info("log1 info")
log1.warning("log1 warning")
log1.error("log1 error")
log1.critical("log1 critical")

# 记录info以上级别的日志，不输出到控制台
log2 = Log(debug=False)
log2.debug("log2 debug")
log2.info("log2 info")
log2.warning("log2 warning")
log2.error("log2 error")
log2.critical("log2 critical")

# 记录error以上级别的日志不输出到控制台
log3 = Log(debug=False, level="ERROR")
log3.debug("log3 debug")
log3.info("log3 info")
log3.warning("log3 warning")
log3.error("log3 error")
log3.critical("log3 critical")
```

### 案例5：日志序列化为JSON

```python
from log import Log

# 记录info级别的日志，并将所有级别日志输出到控制台
log1 = Log(serialize=True, debug=True)
log1.debug("log1 debug")
log1.info("log1 info")
log1.warning("log1 warning")
log1.error("log1 error")
log1.critical("log1 critical")

# 记录info以上级别的日志，不输出到控制台
log2 = Log(serialize=True, debug=False)
log2.debug("log2 debug")
log2.info("log2 info")
log2.warning("log2 warning")
log2.error("log2 error")
log2.critical("log2 critical")
```