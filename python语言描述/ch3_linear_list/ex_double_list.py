from python语言描述.ch3_linear_list.double_list import DDList


class DDListEx(DDList):
    def __init__(self):
        DDList.__init__(self)

    # 移动结点的数据：reverse，sort
    def reverse(self):
        p = self._head
        q = self._rear
        while p is not q and p is not q.next:
            p.elem, q.elem = q.elem, p.elem
            p = p.next
            q = q.prev

    def sort(self):
        p = self._head

        while p is not None:
            q = self._head

            while q is not p and q.elem <= p.elem:
                q = q.next

            value = p.elem
            while q is not p:
                k = q.elem
                q.elem = value
                value = k
                q = q.next
            p.elem = value
            p = p.next

    # 改变结点的连接关系：reverse1，sort1
    def reverse1(self):
        p = self._head
        q = None
        k = self._head.next

        self._head, self._rear = self._rear, self._head
        while k is not None:
            p.prev = k
            p.next = q
            q = p
            p = k
            k = k.next
        p.prev = None
        p.next = q

    def sort1(self):
        pass

    # 基于单链表的排序函数
    def sort_base_single(self):
        super().sort2()
        p = self._head
        q = None

        while p is not None:
            p.prev = q
            q = p
            p = p.next
        q.next = None
        self._rear = q


if __name__ == "__main__":
    mlist1 = DDListEx()
    for i in range(8):
        mlist1.append(i)    # 123...
    mlist1.reverse()
    mlist1.printall()       # 321

    mlist1.sort()
    mlist1.printall()       # 123

    mlist1.reverse1()       # 321
    mlist1.printall()
    print(mlist1._head.elem, mlist1._rear.elem)

    mlist1.sort_base_single()
    mlist1.printall()       # 123
    print(mlist1._head.elem, mlist1._rear.elem)
