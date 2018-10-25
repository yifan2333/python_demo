def count():
    fs = []
    for i in range(1, 4):
        def square():
            return i * i
        fs.append(square)
    return fs


# 计算可变参数的和
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


# 不需要立刻求和，而是在后面的代码中，根据需要再计算，可以不返回求和的结果，而是返回求和的函数
# 我们在函数lazy_sum中又定义了函数sum，
# 并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。
# 当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数
def lazy_sum(*args):
    def my_sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return my_sum


if __name__ == '__main__':
    print(calc_sum(1, 2, 3, 4, 5))
    # 返回的并不是求和结果，而是求和函数
    f = lazy_sum(1, 2, 3, 4, 5)
    print(f)
    # 调用函数f时，才真正计算求和的结果
    print(f())

    f1 = lazy_sum(1, 3, 5, 7, 9)
    f2 = lazy_sum(1, 3, 5, 7, 9)
    print(f1 == f2)

    a, b, c = count()
    # 全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
    print(a)
    print(b)
    print(c)
    print(a())
    print(b())
    print(c())
