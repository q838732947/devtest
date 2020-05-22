from typing import List


def reverse(x: int) -> int:
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


def romanToInt(s: str) -> int:
    d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    d2 = {"IV": "IIII", "IX": "VIIII", "XL": "XXXX", "XC": "LXXXX", "CD": "CCCC", "CM": "DCCCC"}
    for key in d2.keys():
        s = s.replace(key, d2[key])

    print(s)
    sum = 0
    for i in range(len(s)):
        sum += d[s[i]]
    return sum


def longestCommonPrefix(strs: List[str]) -> str:
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


def isValid(s: str) -> bool:
    stack = ["?"]
    dic = {"{": "}", "[": "]", "(": ")"}
    for s0 in s:
        if s0 in dic:
            stack.append(s0)
        else:
            if len(stack) == 1:
                return False
            else:
                if dic[stack.pop()] == s0:
                    continue
                else:
                    return False
    return True


if __name__ == '__main__':
    # print(reverse(123))
    # print(romanToInt("IV"))
    # print(longestCommonPrefix(["flower", "flow", "flight"]))
    print(isValid("{[]"))

