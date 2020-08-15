import random
import time


def create_list(n, range_min=-100, range_max=100):
    l = []
    for i in range(n):
        l.append(random.randint(range_min, range_max))
    print("原始列表：", l)
    return l


def insertion_sort(l):
    # 插入排序，构建有序数列，将待插入元素插入指定位置
    # 时间复杂度：O(n**2) 空间复杂度：O(1)
    if len(l) <= 1: return l
    for i in range(1, len(l)):
        preindex = i - 1
        current = l[i]
        while (preindex >= 0 and l[preindex] > current):
            l[preindex + 1] = l[preindex]
            preindex -= 1
        # print(j)
        l[preindex + 1] = current
    return l


def selection_sort(l):
    # 选择排序，找到最小值，放到对应位置
    # 时间复杂度：O(n**2) 空间复杂度：O(1)
    for i in range(len(l)):
        min_index = i
        for j in range(i + 1, len(l)):
            if l[min_index] > l[j]:
                min_index = j
        if l[i] > l[min_index]:
            l[i], l[min_index] = l[min_index], l[i]
    return l


def bubble_sort(l):
    # 冒泡排序 比对相邻元素，若不符合排序则交换位置
    # 时间复杂度：O(n**2) 空间复杂度：O(1)

    for i in range(len(l)):
        for j in range(len(l) - 1 - i):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l


def p(f, func_desc=""):
    start = time.process_time()
    print(f)
    end = time.process_time()
    print(f"{func_desc}process time is {end - start}s")




def main():
    l = create_list(10, -100, 100)
    p(bubble_sort(l), "冒泡排序")
    p(selection_sort(l), "选择排序")
    p(insertion_sort(l), "插入排序")


if __name__ == '__main__':
    main()
