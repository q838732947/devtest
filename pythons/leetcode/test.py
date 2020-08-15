'''
将数组中所以的0移到末尾，不改变非零元素的位置，不引入新的数组
'''


def f1(listA):
    index = 0
    for i, n in enumerate(listA):
        if n != 0:
            listA[index] = n
            listA[i] = 0
            index += 1
    return listA


'''
返回最后一个单词的单词字数
'''


def f2(s):
    s.strip()
    if s == '': return 0
    s = s.split(' ')
    s.reverse()
    for i in s:
        if i != '':
            return len(i)


'''
给定一个正整数，返回它在 Excel 表中相对应的列名称。
'''


def f3(n):
    if n <= 26:
        return chr(64 + n)
    f1 = int(n / 26)
    f2 = n % 26
    if f2 == 0:
        return chr(64 + f1 - 1) + chr(64 + 26)
    return chr(64 + f1) + chr(64 + f2)


if __name__ == '__main__':
    listA = [0, 1, 0, 3, 0, 0, 8, 9, 0]
    print(f1(listA))
    s = '      '
    print(f2(s))
    print(f3(n=1))
    print(f3(n=52))
