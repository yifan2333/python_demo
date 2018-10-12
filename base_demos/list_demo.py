if __name__ == '__main__':

    # list
    classmates = ['Michael', 'Bob', 'Tracy']
    print(classmates)
    print(len(classmates))
    print(classmates[0])
    print(classmates[-1])  # 最后一个元素
    print(classmates[-2])
    print(classmates[-3])
    classmates.append("Adam")
    print(classmates)
    classmates.insert(1, 'Jack')  # 把元素插入到指定的位置，比如索引号为1的位置
    print(classmates)

    classmates.pop()
    print(classmates)  # 要删除list末尾的元素，用pop()方法

    classmates.pop(1)  # 要删除指定位置的元素，用pop(i)方法，其中i是索引位置
    print(classmates)

    classmates[1] = 'Sarah'
    print(classmates)

    L = ['Apple', 123, True]  # list里面的元素的数据类型也可以不同
    print(L)

    s = ['python', 'java', ['asp', 'php'], 'scheme']
    print(len(s))

    # 另一种有序列表叫元组：tuple。tuple和list非常类似，
    # 但是tuple一旦初始化就不能修改，比如同样是列出同学的名字
    classmates = ('Michael', 'Bob', 'Tracy')
    print(classmates)

    # 要定义一个只有1个元素的tuple t = (1)
    # 这样定义的不是tuple，是1这个数！
    # 这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，
    # 因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1
    t = (1,)
    print(t)
