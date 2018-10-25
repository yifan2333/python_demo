def build(x, y):
    return lambda: x * x + y * y


if __name__ == "__main__":
    # 当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便。
    print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
    print(build(3, 4)())
