from setuptools import setup, find_packages

setup(
    name='zdppy_log',  # 包名字
    version='0.1.0',  # 包版本
    description='生成随机的数据',  # 简单描述
    author='张大鹏520',  # 作者
    author_email='1156956636@qq.com',  # 作者邮箱
    url='https://github.com/zhangdapeng520',  # 包的主页
    packages=find_packages(),  # 包
)

# 打包命令：python setup.py sdist bdist_wheel
