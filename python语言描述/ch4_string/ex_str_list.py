# TODO 没有完全基于链表的结构进行练习,而且复杂度可以优化

from python语言描述.ch3_linear_list.single_list import LList
from python语言描述.ch4_string.KMP import *
from python语言描述.ch4_string.naive_matching import naive_matching


class StrList(LList):
    def __init__(self, string: str):
        super().__init__()
        for i in string:
            self.append(i)

    def len(self):
        return super().len()

    # TODO 尝试完成使用链表，但是替换时因为要考虑old new的长度，无法很好解决这一问题
    # def naive_match(self, p):
    #     h = self._head
    #     m = len(p)
    #     i = 0
    #
    #     while i < m and h is not None:
    #         if p[i] == h.elem:
    #             if i == 0:
    #                 j = h
    #             h = h.next
    #             i += 1
    #
    #         else:
    #             if i == 0:
    #                 h = h.next
    #             else:
    #                 i = 0
    #                 h = j.next
    #     if i == m:
    #         return j
    #     return -1

    # 改用基于python自带str实现
    def replace(self, old: str, new: str, method: str = "kmp", count: int = -1):
        # 拼装string
        h = self._head
        string = ""
        while h is not None:
            string = string + str(h.elem)
            h = h.next

        # 替换string
        m = len(old)
        pnext = gen_next(old)
        k = 1
        while k <= count or count == -1:
            if method == 'kmp':
                matching_res = matching_KMP(string, old, pnext)
                if matching_res == -1:
                    break
                else:
                    string = string[:matching_res] + new + string[matching_res + m:]
            elif method == 'naive':
                matching_res = naive_matching(string, old)
                if matching_res == -1:
                    break
                else:
                    string = string[:matching_res] + new + string[matching_res + m:]
            k += 1

        # 重新设置链表
        self._head = None
        for i in string:
            self.append(i)

    def find_in(self, another):

        # 拼装string
        j = another._head
        string = ""
        while j is not  None:
            string = string + str(j.elem)
            j = j.next

        h = self._head
        k = 0
        while h is not None:
            match_res = naive_matching(string, str(h.elem))
            if match_res == -1:
                h = h.next
            else:
                return k
            k += 1
        return -1

    def find_not_in(self, another):
        # 拼装string
        j = another._head
        string = ""
        while j is not None:
            string = string + str(j.elem)
            j = j.next

        h = self._head
        k = 0
        while h is not None:
            match_res = naive_matching(string, str(h.elem))
            if match_res != -1:
                h = h.next
            else:
                return k
            k += 1
        return -1

    # 移除出现在another中的self全部字符
    def remove(self, another):
        # 一次匹配
        def find_in_node(self, another):

            # 拼装string
            j = another._head
            string = ""
            while j is not None:
                string = string + str(j.elem)
                j = j.next

            while True:
                if self._head is None:    # self没有字符剩余
                    return -1
                if naive_matching(string, self._head.elem) != -1:
                    self._head = self._head.next
                else:
                    break              # 直到self的第一个字符不在string里

            h = self._head
            # 从第二个字符开始检查
            while h.next is not None:
                match_res = naive_matching(string, str(h.next.elem))
                if match_res == -1:
                    h = h.next
                else:
                    return h
            return -1

        while True:
            match_node = find_in_node(self, another)
            if match_node == -1:
                break
            else:
                match_node.next = match_node.next.next


if __name__ == "__main__":
    str1 = StrList('abvcdfgha')
    str1.printall()
    print(str1.len())

    # str1.replace('bc', 'jcj', method='naive')
    # str1.printall()

    str2 = StrList('zxtu')
    print('find in res')
    print(str1.find_in(str2))

    str3 = StrList('abcdfga')
    print('find not in res')
    print(str1.find_not_in(str3))

    print('str1 remove str3')
    str1.remove(str3)
    str1.printall()
