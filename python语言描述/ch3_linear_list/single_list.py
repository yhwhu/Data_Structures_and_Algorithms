# 结点类
# 单链表类，有首结点
# 单链表类，有首尾结点


class ChainedListUnderFlow(ValueError):
    pass


# 结点类
class LNode:
    def __init__(self, elem, next_=None):    # 保存一个元素和一个有下个数据地址（指向下一个数据的内存地址）
        self.elem = elem
        self.next = next_

# # 实现一个链表类
# q = LNode(1)
# p = q                   # p,q 指向同一个内存地址
# for i in range(2, 10):
#     q.next = LNode(i)
#     q = q.next
#
# while p is not None:
#     print(p.elem)
#     p = p.next


# 单链表
class LList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def prepend(self, elem):
        self._head = LNode(elem, self._head)

#         elem.next = self._head   ## 如果elem已经是一个结点类就可以这样写
#         self._head = elem
#
# q = LNode(100)
# p = LList()
# p.prepend(q)
# print(p._head.elem)

    # 删掉第一个结点并返回它
    def pop(self):
        if self._head is None:
            return ChainedListUnderFlow("in pop")

        e = self._head.elem
        self._head = self._head.next
        return e

    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            return
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)

    def pop_last(self):
        if self._head is None:
            raise ChainedListUnderFlow("in pop_last")

        p = self._head
        if p.next is None:
            e = p.elem
            self._head = None
            return e

        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        return e

    def find(self, pred):
        p = self._head
        while p is not None:
            if pred(p.elem):
                return p.elem
            p = p.next

    def printall(self):
        p = self._head
        while p is not None:
            print(p.elem, end='')
            if p.next is not None:
                print(', ', 'end')
            p = p.next 
        print('')
        # print('finish printing')

    # 迭代器
    def elements(self):
        p = self._head
        while p is not None:
            yield p.elem
            p = p.next

    # 生成器 find的改进版本,可以筛选出满足条件的所有数据
    def filter(self, pred):
        p = self._head
        while p is not None:
            if pred(p.elem):
                yield p.elem
            p = p.next

    def reverse(self):  # 改变连接顺序
        p = None
        while self._head is not None:
            q = self._head
            self._head = self._head.next   # 前端删除
            q.next = p                     # 前端插入
            p = q
        self._head = p

    # 练习题
    def len(self):
        count = 0
        p = self._head
        while p is not None:
            count += 1
            p = p.next
        return count

    def insert(self, elem, i):
        if i < 1 or i > self.len():
            raise ChainedListUnderFlow('in insert of LList')

        q = LNode(elem)
        if i == 1:
            q.next = self._head
            self._head = q
        else:
            p = self._head
            for k in range(i-2):
                p = p.next
            q.next = p.next
            p.next = q
        return

    def del_i(self, i):
        if i < 1 or i > self.len():
            raise ChainedListUnderFlow('in insert of LList')

        if i == 1:
            self._head = self._head.next
        else:
            p = self._head
            for k in range(i-2):
                p = p.next
            p.next = p.next.next
        return

    # 插入排序
    # 移动表中元素
    def sort1(self):
        if self._head is None:
            return
        crt = self._head.next
        while crt is not None:
            x = crt.elem
            p = self._head
            while p is not crt and p.elem <= x:
                p = p.next

            while p is not crt:
                y = p.elem
                p.elem = x       # 存入前一个结点的数据
                x = y
                p = p.next
            crt.elem = x
            crt = crt.next

    # 改变结点连接关系
    def sort2(self):
        if self._head is None:
            return

        crt = self._head.next
        self._head.next = None       # TODO  没看懂
        while crt is not None:
            x = crt.elem
            p = self._head
            q = None
            while p is not None and p.elem <= x:
                q = p
                p = p.next

            if q is None:
                self._head = crt
            else:
                q.next = crt
            q = crt
            crt = crt.next
            q.next = p


# 单链表的简单变动，增加一个尾结点,继承所有的非变动操作
class LList1(LList):
    def __init__(self):
        LList.__init__(self)
        self._rear = None

    def prepend(self, elem):
        if self._head is None:        # 统一用head判断表空更合适
            self._head = LNode(elem, None)
            self._rear = self._head   # 表头为空，表尾也必为空
        else:
            self._head = LNode(elem, self._head)

    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            self._rear = self._head
        else:
            self._rear.next = LNode(elem)
            self._rear = self._rear.next

    def pop_last(self):
        if self._head is None:
            raise ChainedListUnderFlow('in pop_last')

        p = self._head
        if p.next is None:
            e = p.elem
            self._head = None
            return e

        while p.next.next is not None:    # 加入尾结点也无法知道前一个结点
            p = p.next
        e = p.next.elem
        p.next = None
        self._rear = p
        return e
    # pop不需要修改，因为是通过head判断表空，所以在0个，1个，几个数据情况下，仍然可以适用。
    # 0个就会报错；1个可以删除，但是表空，后续的其他操作都能检测出表空；多个正常删除，不影响rear

    def reverse(self):  # 改变连接顺序
        self._rear = self._head          # 尾结点重新设置

        p = None
        while self._head is not None:
            q = self._head
            self._head = self._head.next  # 前端删除
            q.next = p                    # 前端插入
            p = q
        self._head = p


if __name__ == "__main__":
    # mlist1 = LList()
    # for i in range(10):
    #     mlist1.prepend(i)
    # for i in range(11, 20):
    #     mlist1.append(i)
    # mlist1.printall()
    # print(mlist1.pop())
    # print(mlist1.pop_last())
    #
    # for x in mlist1.elements():
    #     print(x)
    #
    # mlist2 = LList1()
    # mlist2.prepend(100)
    # mlist2.prepend(200)
    # for i in range(11, 20):
    #     mlist2.append(i)
    #
    # mlist2.printall()      # TODO 打印后总是有个None，不知原因。已解决：print了结果，该函数没有返回值，所以是None
    # print('last:', mlist2.pop_last())
    # print('first:', mlist2.pop())
    #
    # for x in mlist2.filter(lambda y: y % 2 == 0):
    #     print(x)

    mlist3 = LList()
    for i in range(10):
        mlist3.append(i)
    mlist3.reverse()
    print("")
    print("reverse:")
    mlist3.printall()
    #
    mlist3.sort2()
    print("")
    print('sort2')
    mlist3.printall()

    mlist3.reverse()
    mlist3.sort1()
    print("")
    print("sort1")
    mlist3.printall()

    # mlist4 = LList()
    # for i in range(10):
    #     mlist4.append(i)
    #
    # mlist4.del_i(1)
    # mlist4.printall()
    #
    # print('')
    # mlist4.insert(100, 9)
    # mlist4.printall()
