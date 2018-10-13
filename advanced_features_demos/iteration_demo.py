from collections import Iterable

if __name__ == '__main__':
    d = {'a': 1, 'b': 2, 'c': 3}
    for key in d:
        print(key, d[key])

    # 遍历字典的values
    for value in d.values():
        print(value)
    # 要同时迭代key和value
    for k, v in d.items():
        print(k, v)

    # 如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：
    print(isinstance('abc', Iterable))
    print(isinstance([1, 2, 3], Iterable))  # list是否可迭代

    # 如果循环的时候想知道下标，
    # Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身、
    for i, value in enumerate(['A', 'B', 'C']):
        print(i, value)

    # for循环里，同时引用了两个变量，在Python里是很常见的
    for x, y in [(5, 1), (2, 4), (3, 9)]:
        print(x, y)
