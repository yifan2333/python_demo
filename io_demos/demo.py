import os


if __name__ == '__main__':
    print(os.name)  # 操作系统类型
    # print(os.uname())  # 要获取详细的系统信息，注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。
    print(os.environ)  # 环境变量
    print(os.environ.get("path"))
    print(os.path.abspath('.'))