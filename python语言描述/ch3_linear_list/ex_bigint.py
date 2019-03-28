# 基于链表实现整数的各种运算，一个链表是一个整数

from python语言描述.ch3_linear_list.single_list import LList


class BigInt(LList):
    def __init__(self):
        super().__init__()
        # LList.__init__(self)

    def true_number(self):
        # 第一个结点是个位，然后是十位，百位..
        k = 0
        self.num = 0
        p = self._head
        while p is not None:
            self.num += p.elem * 10 ** k
            k += 1
            p = p.next

    def __eq__(self, other):
        self.true_number()
        other.true_number()
        return self.num == other.num

    def __add__(self, other):
        self.true_number()
        other.true_number()
        return self.num + other.num

    def __mul__(self, other):
        self.true_number()
        other.true_number()
        return self.num * other.num


if __name__ == '__main__':
    mlist1 = BigInt()
    mlist2 = BigInt()
    for i in range(2):
        mlist1.append(i)
        mlist2.append(i + 1)

    mlist1.true_number()
    mlist2.true_number()
    print(mlist1.num, mlist2.num)
    print(mlist1 + mlist2)
    print(mlist1 * mlist2)
