def test_case():
    a = [1, 2, 3]
    b = ["a", "b", "c"]
    c = [4, 5, 6]
    l = zip(a, b, c)
    # print(list(l))  # [(1, 'a', 4), (2, 'b', 5), (3, 'c', 6)]
    x, y, z = zip(*l)
    print(x, y, z)  # zip(*)解压:(1, 2, 3) ('a', 'b', 'c') (4, 5, 6)
    a = [1, 2, 3]
    b = ["c", "d"]
    c = zip(a, b)
    print(list(c))  # [(1, 'c'), (2, 'd')] zip 以短的为主
    print(list(c))  # []，zip只能使用一次，因为迭代器的内部指针已经指向了内部的最后一个元组

    # 结合dict造测试请求数据,
    user = ['alan', 'jax', 'zz']
    pwd = ['123', '456', '789']
    test_data = list(zip(user, pwd))
    print(test_data)  # 输出用户名和密码组成的列表[('alan', '123'), ('jax', '456'), ('zz', '789')]
    test_data = dict(test_data)  # 可迭代对象方式来构造字典
    print(test_data)  # {'alan': '123', 'jax': '456', 'zz': '789'}


if __name__ == '__main__':
    test_case()
