# 双链表

from python语言描述.ch3_linear_list.single_list import LNode, LList1, ChainedListUnderFlow

# 双链表结点类
class DLNode(LNode):
    def __init__(self, elem, prev=None, next_=None):
        LNode.__init__(self, elem, next_)
        self.prev = prev


# 双链表类
# 和单链表增加一个尾结点相似，但是双链表的每个结点都是双向的
# TODO 双链表是不是也可以设计为只知道一个首结点？ 应该是可以的
class DDList(LList1):
    def __init__(self):
        LList1.__init__(self)

    def prepend(self, elem):
        p = DLNode(elem, prev=None, next_=self._head)   # 建立p到head的连接
        if self._head is None:
            self._rear = p
        else:
            p.next.prev = p                             # 建立head到p的连接
        self._head = p

    def append(self, elem):
        p = DLNode(elem, prev=self._rear, next_=None)
        if self._head is None:
            self._head = p
        else:
            p.prev.next = p
        self._rear = p

    def pop(self):
        if self._head is None:
            raise ChainedListUnderFlow("in pop of DLList")

        e = self._head.elem
        self._head = self._head.next
        if self._head is not None:
            self._head.prev = None
        return e

    def pop_last(self):
        if self._head is None:
            raise ChainedListUnderFlow("in pop of DLList")

        e = self._rear.elem
        self._rear = self._rear.prev
        if self._rear is not None:
            self._rear.next = None
        else:
            self._head = None            # 判断空表以head为根据,需要多增加一步赋值
        return e

    def reverse(self):
        p = self._head       # 赋值相当于指向同一块内存，后续变更会影响
        q = self._rear

        while p is not q:
            p.elem, q.elem = q.elem, p.elem
            p = p.next
            q = q.prev


if __name__ == "__main__":
    mlist4 = DDList()
    for i in range(10):
        mlist4.prepend(i)
    for i in range(11, 20):
        mlist4.append(i)
    mlist4.printall()
    print("pop:", mlist4.pop())
    print("pop last:", mlist4.pop_last())

    mlist4.reverse()
    mlist4.printall()

