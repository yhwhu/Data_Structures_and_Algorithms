# 循环双链表
# 只需要一个首结点或尾结点即可都是O（1），不用像循环单链表巧妙地使用尾结点的结构

from ch3_linear_list.double_list import DLNode, ChainedListUnderFlow


class DLCList:
    def __init__(self):
        self._head = None
        
    def is_empty(self):
        return self._head is None
    
    def prepend(self, elem):
        if self._head is None:
            self._head = DLNode(elem)
            self._head.prev = self._head
            self._head.next = self._head
        else:
            p = DLNode(elem, self._head.prev, self._head)
            self._head.prev.next = p
            self._head.prev = p
            self._head = p
            
    def append(self, elem):
        self.prepend(elem)
        self._head = self._head.next
    
    def pop(self):
        if self._head is None:
            raise ChainedListUnderFlow("in pop of DLCList")
        
        e = self._head.elem
        if self._head.next is self._head:           # 只有一个结点
            self._head = None
        else:
            self._head.prev.next = self._head.next
            self._head.next.prev = self._head.prev
            self._head = self._head.next
        return e
        
            
    def pop_last(self):
        if self._head is None:
            raise ChainedListUnderFlow("in pop of DLCList")
        
        e = self._head.prev.elem
        if self._head.next is self._head:
            self._head = None
        else:
            self._head.prev.prev.next = self._head
            self._head.prev = self._head.prev.prev   
            # 首结点不变
        return e
    
    def printall(self):
        if self._head is None:
            return
        p = self._head
        while True:
            print(p.elem)
            if p is self._head.prev:
                break
            p = p.next


if __name__ == "__main__":
    mlist5 = DLCList()
    for i in range(10):
        mlist5.prepend(i)
    for i in range(11, 20):
        mlist5.append(i)
    mlist5.printall()
    print("pop:", mlist5.pop())
    print("pop last", mlist5.pop_last())
    print('')

    mlist5.printall()
    print("pop:", mlist5.pop())
    print("pop last", mlist5.pop_last())
