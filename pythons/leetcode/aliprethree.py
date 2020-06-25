# 评测题目: 一个英文文本，统计其中出现次数最多的单词，输出出现前三多的单词以及其出现次数
from typing import List


def func(str):
    s = str.split(' ')
    print(s)
    dic = {}
    for s0 in s:
        if s0 in dic:
            dic[s0] += 1
        if s0 not in dic:
            dic[s0] = 1
    print(dic)

    def take2(elem):
        return elem[1]

    list = []
    for key in dic.keys():
        list.append((key, dic[key]))
    print(list)
    list.sort(key=take2, reverse=True)
    print(list)

    for i in range(len(dic) - 3):
        list.pop()
    return list


def singleNumbers(nums: List[int]) -> List[int]:
    List2 = []
    for i in range(len(nums)):
        if nums[i] in List2:
            List2.remove(nums[i])
        else:
            List2.append(nums[i])
    return List2


if __name__ == '__main__':
    # func()
    print(singleNumbers(nums=[1, 2, 10, 4, 1, 4, 3, 3]))
    str = "a"
    print(str[-1:-len(str) - 1:-1] == str)
    str = "allure hello root jsonpath root jsonpath jsonpath hello hello hello a"
    print(func(str))
