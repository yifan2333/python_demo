if __name__ == '__main__':
    print(sorted([36, 5, -12, 9, -21]))
    print(sorted([36, 5, -12, 9, -21], key=abs))
    L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
    print(sorted(L, key=lambda x: x[0].lower()))
