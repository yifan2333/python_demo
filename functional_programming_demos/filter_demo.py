def is_odd(n):
    return n % 2 == 1


def not_empty(s):
    return s and s.strip()


# 构造一个从3开始的奇数序列
def _odd_iter():
    index = 1
    while True:
        index = index + 2
        yield index


# 定义一个筛选函数
def _not_divisible(n):
    return lambda x: x % n > 0


# 定义一个生成器，不断返回下一个素数
def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        index = next(it)  # 返回序列的第一个数
        yield index
        it = filter(_not_divisible(index), it)  # 构造新序列


def is_palindrome(s):
    a = str(s)
    b = -1
    for index in range(len(a) // 2):
        if a[index] != a[b]:
            return False
        b = b - 1
    return True


if __name__ == '__main__':
    # filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
    print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))

    print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))
    # filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list

    # 打印1000以内的素数:
    for n in primes():
        if n < 1000:
            print(n)
        else:
            break

    #        print(list(filter(is_palindrome, range(1, 200))))

    print(is_palindrome(12))

    output = filter(is_palindrome, range(1, 1000))
    print('1~1000:', list(output))
    if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99,
                                                      101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
        print('测试成功!')
    else:
        print('测试失败!')


