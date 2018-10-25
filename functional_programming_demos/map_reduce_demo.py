from functools import reduce

digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def f(x):
    return x * x


def add(x, y):
    return x + y


def fn(x, y):
    return x * 10 + y


def char2num(s):
    return digits[s]


def str2int(s):
    def in_fn(x, y):
        return x * 10 + y

    def in_char2num(char):
        return digits[char]

    return reduce(in_fn, map(in_char2num, s))


def str2int2(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


if __name__ == '__main__':
    # map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，
    # 并把结果作为新的Iterator返回。
    # map()传入的第一个参数是f，即函数对象本身。
    # 由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。
    r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(list(r))

    # 把这个list所有数字转为字符串：
    print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

    print(reduce(add, [1, 3, 5, 7, 9]))

    # 字符串str也是一个序列，配合map()，就可以写出把str转换为int的函数
    print(reduce(fn, map(char2num, '13579')))

    print(str2int("1212855"))

    print(str2int2("213181551"))
