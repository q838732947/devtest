"""
最长公共前缀
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-prefix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []: return ""
        if len(strs) == 1: return strs[0]
        minl = len(strs[0])
        mins = strs[0]
        for str in strs:
            l = len(str)
            if minl > l:
                minl = l
                mins = str
        record = -1
        stop = 0
        for i in range(minl):
            if stop == 1: break
            for s in strs:
                if s[i] != str[i]:
                    stop = 1
                    break
            if stop == 1:
                break
            else:
                record = i

        if record == -1:
            return ""

        else:
            s = ""
            for i in range(record + 1):
                s += mins[i]
            return s


if __name__ == '__main__':
    print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
    print(Solution().longestCommonPrefix(["dog", "racecar", "car"]))
