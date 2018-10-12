if __name__ == '__main__':
    # dict
    # dict在内部就可以直接计算出Michael对应的存放成绩的“页码”，也就是95这个数字存放的内存地址，直接取出来，所以速度非常快。
    # dict内部存放的顺序和key放入的顺序是没有关系的。
    # dict的key必须是不可变对象。
    d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
    print(d['Michael'])

    d['Michael'] = 90  # 把数据放入dict的方法，除了初始化时指定外，还可以通过key放入
    print(d['Michael'])

    # 由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉
    d['Jack'] = 90
    d['Jack'] = 88
    print(d['Jack'])

    # 如果key不存在，dict就会报错： KeyError: 'Tomas'
    # print(d['Tomas'])

    # 通过in判断key是否存在：
    print('Tomas' in d)

    # 通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value
    print(d.get('Thomas'))
    print(d.get('Thomas', -1))

    # 要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
    print(d.pop("Bob"))

    # 和list比较，dict有以下几个特点：
    # 查找和插入的速度极快，不会随着key的增加而变慢；
    # 需要占用大量的内存，内存浪费多。

    # 而list相反：
    # 查找和插入的时间随着元素的增加而增加；
    # 占用空间小，浪费内存很少。

    # set  s = set([1, 2, 3])  或者  s = {1, 2, 3}
    # set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
    s = {1, 2, 3}
    print(s)

    s = {1, 1, 2, 2, 3, 3}
    print(s)

    s.add(4)
    s.add(4)
    print(s)

    s.remove(4)
    print(s)

    s1 = {1, 2, 3}
    s2 = {2, 3, 4}
    print(s1 & s2)  # 交集
    print(s1 | s2)  # 并集
