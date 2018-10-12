if __name__ == '__main__':
    print('包含中文的str')
    print(ord("A"))
    print(ord("中"))
    print(chr(66))  # 十进制
    print(chr(25991))  # 十进制
    print('\u4e2d\u6587')  # 十六进制

    x = b'A'  # 以字节为单位
    y = 'A'  # 字符
    print(x)
    print(y)
    print(x == y)

    # 纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes。
    # 含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围
    # 以Unicode表示的str通过encode()方法可以编码为指定的bytes
    print('ABC'.encode('ascii'))
    print('中文'.encode('utf-8'))

    # 如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法
    # 如果bytes中包含无法解码的字节，decode()方法会报错
    print(b'ABC'.decode('ascii'))
    print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

    # 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节
    print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))
