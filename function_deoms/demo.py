import math


def my_abs(x1):
    # 数据类型检查可以用内置函数isinstance()实现：
    if not isinstance(x1, (int, float)):
        raise TypeError('bad operand type')
    if x1 >= 0:
        return x1
    else:
        return -x1


# 返回多个值
# 比如在游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的新的坐标
# 但其实这只是一种假象，Python函数返回的仍然是单一值
# 原来返回值是一个tuple！
# 但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，
# 所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。
def move(x1, y1, step, angle=.0):
    nx = x1 + step * math.cos(angle)
    ny = y1 - step * math.sin(angle)
    return nx, ny


def nop():
    pass


# 位置参数 (x1, n)
# 默认参数 (x1, n=2)
def power(x1, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x1
    return s


# 默认参数很有用，但使用不当，也会掉入坑里。默认参数有个最大的坑
# 定义默认参数要牢记一点：默认参数必须指向不变对象！
def add_end(L=[]):
    L.append('END')
    return L


# 我们可以用None这个不变对象来实现：
def add_end2(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


# 可变参数 (*numbers)
def calc(*numbers):
    my_sum = 0
    for n1 in numbers:
        my_sum = my_sum + n1 * n1
    return my_sum


# 关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
# 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查。
def person(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:', name, 'age:', age, 'other:', kw)


# 命名关键字参数
# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下
# 命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错 (name, age, *, city, job)
# 命名关键字参数可以有缺省值，从而简化调用  (name, age, *, city='Beijing', job)
def person2(name, age, *, city='Beijing', job):
    print(name, age, city, job)


# 参数组合
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


# 递归函数
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


# 汉诺塔的移动
def move2(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move2(n-1, a, c, b)
        move2(1, a, b, c)
        move2(n-1, b, a, c)


if __name__ == '__main__':
    print(abs(100))
    print(abs(-20))
    print(max(2, 3, 1, -5))
    print(int('123'))

    # 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
    a = abs
    print(a(-1))

    print(my_abs(-1))
    # print(my_abs('A'))

    x, y = move(100, 100, 60, math.pi / 6)
    print(x, y)

    print(power(5))
    print(power(5, 2))

    print(add_end([1, 2, 3]))
    print(add_end(['x', 'y', 'z']))

    # 默认参数是[]，但是函数似乎每次都“记住了”上次添加了'END'后的list。
    for n in range(5):
        print(add_end())

    for n in range(5):
        print(add_end2())

    print(calc(1, 2, 3, 4))

    nums = [1, 2, 3, 4, 5]
    print(calc(*nums))

    person('Michael', 30)
    person('Bob', 35, city='Beijing')
    person('Adam', 45, gender='M', job='Engineer')

    extra = {'city': 'Beijing', 'job': 'Engineer'}
    person('Jack', 24, **extra)

    person2('Jack', 24, city='Beijing', job='Engineer')
    person2('Jack', 24, job='Engineer')

    f1(1, 2)
    f1(1, 2, c=3)
    f1(1, 2, 3, 'a', 'b')
    f1(1, 2, 3, 'a', 'b', x=99)
    f2(1, 2, d=99, ext=None)

    print(fact(12))

    move2(3, 'A', 'B', 'C')
