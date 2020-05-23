"""
整数反转
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:
输入: 123
输出: 321
 示例 2:
输入: -123
输出: -321
示例 3:
输入: 120
输出: 21
注意:
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2**31,  2**31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

链接：https://leetcode-cn.com/problems/reverse-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            s = list(str(x))
            s.reverse()
            r = [str(i) for i in s]
            r = int("".join(r))
        elif x < 0:
            x = abs(x)
            s = list(str(x))
            s.reverse()
            r = [str(i) for i in s]
            r = int("-" + "".join(r))
        if r < 2 ** 31 - 1 and r > -2 ** 31:
            return r
        else:
            return 0


if __name__ == '__main__':
    print(Solution().reverse(123))
    print(Solution().reverse(-123))
    print(Solution().reverse(120))
    print(Solution().reverse(1234567892))
