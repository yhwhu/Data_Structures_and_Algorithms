# 基于python自带str的练习

from python语言描述.ch4_string.KMP import *


class MyString:
    def __init__(self, string):
        self.string = str(string)

    def replace(self, old: str, new: str, count: int = -1):
        m = len(old)
        pnext = gen_next(old)

        k = 1
        while k <= count or count == -1:
            matching_res = matching_KMP(self.string, old, pnext)
            if matching_res == -1:
                break
            else:
                self.string = self.string[:matching_res] + new + self.string[matching_res + m:]
            k += 1


# 分隔符sep,将string用sep分隔
def tokens(string, seps):
    m = len(seps)
    pnext = gen_next(seps)

    seps_res = []
    while True:
        matching_res = matching_KMP(string, seps, pnext)
        if matching_res == -1:                          # 没有匹配分隔符时
            seps_res.append(string)
            break
        if matching_res == 0:                           # 去掉前缀相同的部分
            string = string[m:]
            continue
        seps_res.append(string[:matching_res])
        string = string[matching_res+m:]
    return seps_res


if __name__ == "__main__":
    str1 = MyString('abcdefgab')
    print(str1.string)

    str1.replace('a', 'A')
    print(str1.string)

    str2 = str('afabcdafabcafghjfafiop')
    sep1 = str('af')
    res = tokens(str2, sep1)
    print(res)
