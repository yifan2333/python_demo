if __name__ == '__main__':
    L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
    # 取前3个元素
    print(L[0])
    print(L[1])
    print(L[2])

    r = []
    n = 3
    for i in range(n):
        r.append(L[i])
    print(r)

    # 使用切片特性
    # L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。
    print(L[0:3])
    # 如果第一个索引是0，还可以省略：
    print(L[:3])
    # 类似的，既然Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片
    # 记住倒数第一个元素的索引是-1。
    print(L[-2:])
    print(L[-2:-1])

    L = list(range(100))
    print(L)
    # 前10个数
    print(L[:10])
    # 后10个数
    print(L[-10:])
    # 前11-20个数
    print(L[10:20])
    # 前10个数，每两个取一个
    print(L[:10:2])
    # 所有数，每5个取一个
    print(L[::5])
    # 什么都不写，只写[:]就可以原样复制一个list
    print(L[:])
    # tuple也是一种list，唯一区别是tuple不可变。
    # 因此，tuple也可以用切片操作，只是操作的结果仍是tuple
    print((1, 2, 3, 4, 5, 6, 7, 8, 9)[:3])
    # 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。
    # 因此，字符串也可以用切片操作，只是操作结果仍是字符串
    print('ABCDEFG'[:3])