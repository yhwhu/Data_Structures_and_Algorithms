# 循环单链表,尾结点rear指向表头。

from ch3_linear_list.chained_list_a import LNode, ChainedListUnderFlow


class LCList:
    def __init__(self):
        self._rear = None

    def is_empty(self):
        return self._rear is None

    def prepend(self, elem):
        p = LNode(elem)

        if self._rear is None:   # 空表
            p.next = p           # 构成环
            self._rear = p
        else:
            p.next = self._rear.next  # p的下一个结点是表头结点，即rear指向的结点
            self._rear.next = p      # p此时是表头结点，更改rear的指向

    def append(self, elem):
        p = LNode(elem, self._rear.next)  # 没有考虑空表的情况
        self._rear.next = p
        self._rear = p

        # self.prepend(elem)
        # self._rear = self._rear.next

    def pop(self):
        if self._rear is None:
            raise ChainedListUnderFlow("in pop of LCList")

        p = self._rear.next
        e = p.elem

        if self._rear is p:     # 此时没有结点了
            self._rear = None
        else:
            self._rear.next = self._rear.next.next
        return e

    def printall(self):
        if self._rear is None:
            return
        p = self._rear.next
        while True:
            print(p.elem)
            if p is self._rear:
                break
            p = p.next
            # print(p is not self._rear)


if __name__ == "__main__":
    mlist3 = LCList()
    for i in range(10):
        mlist3.prepend(i)
    for i in range(11, 20):
        mlist3.append(i)
    mlist3.printall()
    print("pop:", mlist3.pop())


