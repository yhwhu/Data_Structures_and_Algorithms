from python语言描述.ch3_linear_list.single_list import LList


class LListEx(LList):
    def __init__(self):
        LList.__init__(self)

    # 反转遍历进行op操作，反转+遍历+反转
    def rev_visit(self, op):
        p = None
        while self._head is not None:
            q = self._head
            self._head = self._head.next
            q.next = p
            p = q
        self._head = p

        p2 = self._head
        while p2 is not None:
            p2.elem = op(p2.elem)
            p2 = p2.next

        self.printall()  # 链表已经反转
        p = None
        while self._head is not None:
            q = self._head
            self._head = self._head.next
            q.next = p
            p = q
        self._head = p

    # 删除最小的数，保持相对顺序
    def del_minimal(self):
        p = self._head
        if p.next is None:
            self._head = None

        q = self._head
        minnum = q.elem
        while p.next is not None:
            if p.next.elem < minnum:
                minnum = p.next.elem
                q = p
            p = p.next

        if q is self._head:      # 恰好第一个数据最小
            self._head = self._head.next
        else:
            q.next = q.next.next

    # 删除重复的数，第一次出现的保持不动
    def del_duplicate(self):
        p = self._head
        dataset = {p.elem}       # 集合
        while p.next is not None:
            if p.next.elem in dataset:
                p.next = p.next.next
            else:
                dataset.add(p.next.elem)
                p = p.next

    # 与另外一个链表交错
    def interleaving(self, another):
        p = self._head
        q = another._head

        while p.next is not None and q.next is not None:
            t = q.next
            q.next = p.next
            p.next = q
            p = p.next.next
            q = t

        if p.next is None:
            p.next = q
        else:
            q.next = p.next
            p.next = q


# 单链表剖分函数，一个满足pred，一个不满足pred
def partition(lst, pred):
    res1 = LListEx()
    res2 = LListEx()

    p = lst._head
    while p is not None:
        if pred(p.elem):
            res1.append(p.elem)
        else:
            res2.append(p.elem)
        p = p.next
    return res1, res2


if __name__ == "__main__":

    # mlist = LListEx()
    # for i in range(10):
    #     mlist.append(i)
    # # mlist.printall()
    #
    # print('reverse visit')
    # mlist.rev_visit(lambda x: x*100)
    # mlist.printall()
    #
    # print('del minimal')
    # mlist.del_minimal()
    # mlist.printall()

    # mlist2 = LListEx()
    # for i in [5, 1, 2, 4, 3]*6:
    #     mlist2.append(i)
    # mlist2.printall()
    #
    # print('dulete duplicate')
    # mlist2.del_duplicate()
    # mlist2.printall()

    # mlist3 = LListEx()
    # mlist4 = LListEx()
    # for i in range(3):
    #     mlist3.append(2*i)
    #     mlist3.append(30)
    #     mlist4.append(2*i+1)
    #     # mlist4.append(30)
    # print('mlist3')
    # mlist3.printall()
    # print('mlist4')
    # mlist4.printall()
    # print('inter')
    # mlist3.interleaving(mlist4)
    # mlist3.printall()

    mlist5 = LListEx()
    for i in range(10):
        mlist5.prepend(i)
    # mlist5.printall()

    res1, res2 = partition(lst=mlist5, pred=lambda x: x % 3 == 0)
    print('res1')
    res1.printall()
    print('res2')
    res2.printall()