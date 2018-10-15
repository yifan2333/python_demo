def fib2(max_value):
    index, a, b = 0, 0, 1
    while index < max_value:
        yield b
        a, b = b, a + b
        index = index + 1
    return 'done'


def fib(max_value):
    index, a, b = 0, 0, 1
    while index < max_value:
        print(b)
        a, b = b, a + b
        index = index + 1
    return 'done'


if __name__ == '__main__':

    # 通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的
    # 而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，
    # 如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了
    # 如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
    # 这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator
    # 要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator

    g = (x * x for x in range(10))
    print(g)  # <generator object <genexpr> at 0x0000021860D20228>
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))

    # generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。

    # 上面这种不断调用next(g)实在是太变态了，正确的方法是使用for循环，因为generator也是可迭代对象
    g = (x * x for x in range(10))
    for n in g:
        print(n)

    fib(6)

    g = fib2(6)  # <generator object fib2 at 0x0000026981A20228>
    print(g)
    for n in g:
        print(n)
