from python语言描述.ch3_linear_list.single_list import LNode


class StackUnderflow(ValueError):
    pass


# 栈的顺序表实现
class SStack:

    def __init__(self):
        self._elems = []

    def is_empty(self):
        return self._elems == []

    def top(self):
        if self._elems == []:
            raise StackUnderflow("in SStack.top()")
        return self._elems[-1]

    def push(self, elem):
        self._elems.append(elem)

    def pop(self):
        if self._elems == []:
            raise StackUnderflow("in SStack.pop()")
        return self._elems.pop()


# 栈的链接表实现
class LStack():

    def __init__(self):
        self._top = None

    def is_empty(self):
        return self._top is None

    def top(self):
        if self._top is None:
            raise StackUnderflow("in LStack.top()")

    def push(self, elem):
        self._top = LNode(elem, next_=self._top)

    def pop(self):
        if self._top is None:
            raise StackUnderflow("in LStack.pop()")
        head = self._top
        self._top = self._top.next
        return head.elem


def check_parens(text):
    """括号配对检查函数，text是被检查的正文串"""
    parens = "()[]{}"
    open_parens = "([{"
    opposite = {")": "(", "]": "[", "}": "{"}

    def parentheses(text):
        """括号生成器，每次调用返回text里的下一括号及其位置"""
        i, text_len = 0, len(text)
        while True:
            while i < text_len and text[i] not in parens:
                i += 1
            if i == text_len:
                return
            yield text[i], i
            i += 1

    st = SStack()
    for pr, i in parentheses(text):
        if pr in open_parens:
            st.push(pr)
        elif opposite[pr] != st.pop():
            print("Unmatching is found at", i, "for", pr)
            return False
    print("All parentheses are correctly matched.")
    return True


def knap_rec(weight, wlist, n):
    """
    递归法解决背包问题
    weight：总重量
    wlist：物品清单
    n：物品数
    """
    if weight == 0:
        return True
    if weight < 0 or (weight > 0 and n < 1):
        return False
    if knap_rec(weight - wlist[n-1], wlist, n-1):
        print("Item" + str(n) + ":", wlist[n-1])
        return True
    if knap_rec(weight, wlist, n-1):
        return True
    else:
        return False


if __name__ == "__main__":
    s1 = SStack()
    s1.push(4)
    s1.push(5)
    # while not s1.is_empty():
    #     print(s1.pop())

    s2 = LStack()
    s2.push(1)
    s2.push(2)
    # while not s2.is_empty():
    #     print(s2.pop())

    # check_parens("(I say( )I say}")

    knap_rec(10, [3, 4, 2, 5, 9], 5)
