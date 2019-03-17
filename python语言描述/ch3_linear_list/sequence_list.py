class SequenceListUnderFlow(ValueError):
    pass


class List:
    def __init__(self):
        self.elements = []

    def len(self):
        return len(self.elements)

    def is_empty(self):
        if self.len() == 0:
            return True
        else:
            return False

    def append(self, elem):
        self.elements.append(elem)

    def prepend(self, elem):
        self.elements = [elem] + self.elements

    def insert(self, elem, i):
        if i < 0:
            raise SequenceListUnderFlow("i is less than 0")
        elif i > len(self.elements):
            raise SequenceListUnderFlow("i is more than length")

        self.elements = self.elements[:i-1] + [elem] + self.elements[i-1:]

    def del_first(self):
        if self.len() == 0:
            return SequenceListUnderFlow("list length is 0")
        self.elements = self.elements[1:]

    def del_last(self):
        if self.len() == 0:
            return SequenceListUnderFlow("list length is 0")
        self.elements = self.elements[:-1]

    def del_i(self, i):
        if self.len() == 0:
            raise SequenceListUnderFlow("list length is 0")
        if i < 1:
            raise SequenceListUnderFlow("i is less than 0")
        elif i > self.len():
            raise SequenceListUnderFlow("i is more than length")
        self.elements = self.elements[:i-1] + self.elements[i:]

    def search(self, num):
        for ind, elem in enumerate(self.elements):
            if elem == num:
                return ind
        return -1

    def reverse(self):
        i, j = 0, self.len() - 1
        while i < j:
            self.elements[i], self.elements[j] = self.elements[j], self.elements[i]
            i, j = i + 1, j - 1

    def list_sort(self):
        for i in range(1, self.len()):
            x = self.elements[i]
            j = i
            while j > 0 and self.elements[j - 1] > x:
                self.elements[j] = self.elements[j - 1]
                j -= 1
            self.elements[j] = x


if __name__ == "__main__":
    lst = List()
    for i in range(8):
        lst.append(i)
    print(lst.elements)

    lst.is_empty()
    lst.insert(elem=10, i=1)
    lst.del_last()
    lst.del_i(i=2)
    print(lst.elements)

    print(lst.search(3))
    print(lst.search(30))

    # print(lst.del_i(i=10))

    lst.reverse()
    print(lst.elements)

    lst.list_sort()
    print(lst.elements)
