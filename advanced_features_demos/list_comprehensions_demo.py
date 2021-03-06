import os

if __name__ == '__main__':
    # 列表生成式即List Comprehensions，
    # 是Python内置的非常简单却强大的可以用来创建list的生成式
    print(list(range(1, 11)))

    # 要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做
    L = []
    for x in range(1, 11):
        L.append(x * x)

    print(L)

    # 循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list
    print([x * x for x in range(1, 11)])

    # for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方
    print([x * x for x in range(1, 11) if x % 2 == 0])

    # 还可以使用两层循环，可以生成全排列
    print([m + n for m in "ABC" for n in "XYZ"])

    # os.listdir可以列出文件和目录
    print([d for d in os.listdir('.')])

    # 列表生成式也可以使用两个变量来生成list
    d = {'x': 'A', 'y': 'B', 'z': 'C'}
    print([x + y for x, y in d.items()])

    # 最后把一个list中所有的字符串变成小写
    L = ['Hello', 'World', 'IBM', 'Apple']
    print([x.lower() for x in L])
