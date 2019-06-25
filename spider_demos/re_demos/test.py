from functools import reduce


def printCode(mystr):
    print(reduce(lambda x, y: x + y, map(hex, map(ord, mystr))).replace('0x', '\\u'))


def printStr(code):
    print(code)


if __name__ == '__main__':
    printCode('刘筱雨喝咖啡吗')
    printStr('\u5218\u7b71\u96e8\u559d\u5496\u5561\u5417')
