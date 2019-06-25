class Ball:
    def __init__(self, name):
        self.name = name

    def kick(self):
        print("我叫%s" % self.name)


class Person:
    # 属性前边加上 __ 会变成私有属性
    # 私有属性可以通过_className__属性名来访问  比如 p._Person__name
    __name = "吴一凡"

    def get_name(self):
        return self.__name


class Parent:
    def hello(self):
        print("正在调用父类的方法")


class Child(Parent):
    def hello(self):
        print("正在调用子类的方法")


class C:
    def __init__(self, size=10):
        self.size = size

    def getSize(self):
        return self.size

    def setSize(self, value):
        self.size = value

    def delSize(self):
        del self.size

    x = property(getSize, setSize, delSize)


class Rectangle:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getPeri(self):
        return (self.x + self.y) * 2

    def getArea(self):
        return self.x * self.y


class CapStr(str):
    def __new__(cls, string):
        string = string.upper()
        return str.__new__(cls, string)


# class int(int):
#     def __add__(self, other):
#         return int.__sub__(self, other)
class Nint(int):
    # 反运算：a + b python解释器从对象a中找 __add__ 方法，
    # 如果找不到，会去 b 中找__radd__方法 如 1 + int(5)就是执行int(5)的__radd()__方法
    def __radd__(self, other):
        return int.__sub__(self, other)


class MyDescriptor:
    def __get__(self, instance, owner):
        print("getting...", self, instance, owner)

    def __set__(self, instance, value):
        print("setting...", self, instance, value)

    def __delete__(self):
        print("deleting...", self)


class MyProperty:
    def __init__(self, fget=None, fset=None, fdel=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, instance, owner):
        return self.fget(instance, owner)

    def __set__(self, instance, value):
        self.fset(instance, value)

    def __delete__(self, instance):
        self.fdel(instance)


class Test:
    x = MyDescriptor()


if __name__ == '__main__':
    test = Test()
    test.x

    b = Ball("吴一凡")
    b.kick()
    p = Person()
    print(p.get_name())
    print(p._Person__name)

    p = Parent()
    p.hello()

    c = Child()
    c.hello()

    c1 = C()
    print(c1.size)
    print(c1.x)
    c1.x = 12
    print(c1.x)
    del c1.x
    print(getattr(c1, "size", None))

    rect = Rectangle(3, 4)
    print(rect.getArea())
    print(rect.getPeri())

    a = CapStr("i love fish")
    print(a)

    a = int(5)
    b = int(3)
    print(a + b)

    a = Nint(5)
    b = Nint(3)
    print(a + b)
    print(1 + b)
