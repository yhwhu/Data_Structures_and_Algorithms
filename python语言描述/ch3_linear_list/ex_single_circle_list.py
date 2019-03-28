# 单循环表的习题
from python语言描述.ch3_linear_list.single_circle_list import LCList


class LCList2(LCList):
    def __init__(self):
        LCList.__init__(self)

    def pop_last(self):
        e = self._rear.elem
        p = self._rear

        if p.next is self._rear:       # 只有一个结点时
            self._rear = None
            return e

        while p.next is not self._rear:
            p = p.next

        p.next = p.next.next
        self._rear = p
        return e

    def filter(self, pred):
        p = self._rear.next

        while True:                 # 循环表的遍历终止条件往往通过if退出
            if pred(p.elem):
                yield p.elem
            if p is self._rear:
                break
            p = p.next

    def reverse(self):
        q = None
        k = self._rear.next
        self._rear = k
        while True:
            p = k
            k = k.next
            p.next = q
            q = p
            if k.next is self._rear:
                break
        k.next = p
        self._rear.next = k

    def sort(self):
        q = self._rear.next

        while True:
            p = self._rear.next
            q = q.next
            while p is not q and p.elem <= q.elem:
                p = p.next

            value = q.elem
            while p is not q:
                k = p.elem
                p.elem = value
                value = k
                p = p.next
            q.elem = value
            if q is self._rear:
                break

    def interleaving(self, another):
        p = self._rear.next
        head = p
        q = another._rear.next

        while True:
            t = q.next
            q.next = p.next
            p.next = q
            p = p.next.next
            q = t
            if p is self._rear or q is another._rear:
                break

        if p is self._rear:
            p.next = q
            self._rear = another._rear
            self._rear.next = head
        else:
            q.next = p.next
            p.next = q

    def rev_visit(self, pred):
        self.reverse()
        p = self._rear.next
        while True:
            if p is self._rear:
                break
            p.elem = pred(p.elem)
            p = p.next

        self.printall()
        self.reverse()

    def del_minimal(self):
        p = self._rear.next
        q = None
        minnum = p.elem
        while True:
            if p is self._rear:
                break
            if p.next.elem < minnum:
                minnum = p.next.elem
                q = p
            p = p.next

        if q is None:                             # 最小数是第一个
            self._rear.next = self._rear.next.next
        elif q.next is self._rear:                # 最小数是最后一个
            q.next = q.next.next
            self._rear = q
        else:
            q.next = q.next.next

    def del_duplicate(self):

        p = self._rear.next
        dataset = {p.elem}

        while True:
            # print('elem', p.next.elem)
            if p.next.elem in dataset:
                p.next = p.next.next
            else:
                dataset.add(p.next.elem)
                p = p.next
            if p.next is self._rear.next:
                break
        self._rear = p


def partition(lst, pred):
    res1 = LCList2()
    res2 = LCList2()

    p = lst._rear.next
    while True:
        if pred(p.elem):
            res1.append(p.elem)
        else:
            res2.append(p.elem)
        p = p.next
        if p is lst._rear.next:
            break
    return res1, res2


if __name__ == "__main__":
    # mlist1 = LCList2()
    # for i in range(10):
    #     mlist1.append(i)
    # mlist1.printall()
    #
    # print("last:", mlist1.pop_last())
    # mlist1.printall()
    #
    # print("filter")
    # for k in mlist1.filter(lambda x: x % 3 == 0):
    #     print(k)

    # mlist2 = LCList2()
    # for i in range(10):
    #     mlist2.append(i)
    # mlist2.reverse()
    # mlist2.printall()
    #
    # print("sort")
    # mlist2.sort()
    # mlist2.printall()

    # mlist3 = LCList2()
    # mlist4 = LCList2()
    # for i in range(3):
    #     mlist3.append(2*i)
    #     mlist3.append(30)
    #     mlist4.append(2*i+1)
    #     # mlist4.append(30)
    # mlist3.printall()
    # mlist3.interleaving(mlist4)
    # print('interleaving')
    # mlist3.printall()
    # print(mlist3._rear.next.elem)

    # mlist5 = LCList2()
    # for i in range(10):
    #     mlist5.append(i)
    # mlist5.rev_visit(lambda x: x * 100)
    # print('rev visit')
    # mlist5.printall()
    #
    # mlist5.del_minimal()
    # print('del minimal')
    # mlist5.printall()

    mlist6 = LCList2()
    for i in [1, 2 , 3]*4 + [4, 5, 6]*8:
        mlist6.append(i)
    mlist6.del_duplicate()
    mlist6.printall()

    res1, res2 = partition(lst=mlist6, pred=lambda x: x%2 == 0)
    print('res1')
    res1.printall()
    print('res2')
    res2.printall()
