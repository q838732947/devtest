def palouti(n: int):
    """
    楼梯数1=<n<=1000，每次可爬1、2梯,打印所有爬法
    eg：
    n=1,1
    n=2,11,2
    n=3,111,12,21,3
    n=4,1111,112,121,1121,13,31 n=1 和3的组合
    n=5,11111,11112,11121,11211,12111,21111,113,131,311,32,23 n=2 和3的组合
    """
    result = {1: ([1],), 2: ([1, 1], [2]), 3: ([1, 1, 1], [1, 2], [2, 1], [3])}
    for i in range(4, n + 1):
        s1 = tuple(j + k for j in result[i - 1] for k in result[1])
        s2 = tuple(j + k for j in result[i - 2] for k in result[2])
        s3 = tuple(j + k for j in result[i - 3] for k in result[3])
        a = []
        [a.append(i) for i in s1 + s2 + s3 if i not in a]
        result[i] = tuple(a)
        print(f"n={i}(合计{len(result[i])}种组合):\n{result[i]}")
    return result[n]


if __name__ == '__main__':
    palouti(6)
