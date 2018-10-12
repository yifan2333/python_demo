if __name__ == '__main__':
    names = ['Michael', 'Bob', 'Tracy']
    for name in names:
        print(name)

    my_sum = 0
    for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        my_sum = my_sum + x
    print(my_sum)

    print(range(5))
    print(list(range(5)))

    my_sum = 0
    n = 99
    while n > 0:
        my_sum = my_sum + n
        n = n - 2
    print(my_sum)

    n = 1
    while n <= 100:
        if n > 10:  # 当n = 11时，条件满足，执行break语句
            break  # break语句会结束当前循环
        print(n)
        n = n + 1
    print('END')

    n = 0
    while n < 10:
        n = n + 1
        if n % 2 == 0:  # 如果n是偶数，执行continue语句
            continue  # continue语句会直接继续下一轮循环，后续的print()语句不会执行
        print(n)