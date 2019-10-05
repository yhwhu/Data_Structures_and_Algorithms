from python语言描述.ch3_linear_list.single_list import LNode


class QueueUnderflow(ValueError):
    pass


class LQueue:

    def __init__(self):
        self._top = None
        self._bottom = None

    def is_empty(self):
        return self._top is None

    def enqueue(self, elem):
        if self._top is None:
            self._top = LNode(elem)
            self._bottom = self._top
        else:
            self._bottom.next = LNode(elem)
            self._bottom = self._bottom.next

    def dequeue(self):
        if self._top is None:
            raise QueueUnderflow("in LQueue.dequeue()")
        head = self._top
        self._top = self._top.next
        return head.elem

    def peek(self):
        if self._top is None:
            raise QueueUnderflow("in LQueue.dequeue()")
        return self._top.elem


class SQueue:

    def __init__(self, init_len=8):
        self._len = init_len
        self._elems = [0]*init_len
        self._head = 0
        self._num = 0

    def is_empty(self):
        return self._num == 0

    def enqueue(self, elem):
        if self._num == self._len:
            self.__extend()
        self._elems[(self._head + self._num) % self._len] = elem
        self._num += 1

    def dequeue(self):
        if self._num == 0:
            return QueueUnderflow("in SQueue.dequeue()")
        elem = self._elems[self._head]
        self._head = (self._head + 1) % self._len
        self._num -= 1
        return elem

    def peek(self):
        if self._num == 0:
            return QueueUnderflow("in SQueue.dequeue()")
        return self._elems[self._head]

    def __extend(self):
        old_len = self._len
        self._len *= 2
        new_elems = [0] * self._len
        for i in range(old_len):
            new_elems[i] = self._elems[(self._head + i) % old_len]
        self._elems, self._head = new_elems, 0


if __name__ == "__main__":
    l1 = LQueue()
    l1.enqueue(1)
    l1.enqueue(2)
    # while not l1.is_empty():
    #     print(l1.dequeue())

    l2 = SQueue()
    l2.enqueue(10)
    l2.enqueue(20)
    while not l2.is_empty():
        print(l2.dequeue())

