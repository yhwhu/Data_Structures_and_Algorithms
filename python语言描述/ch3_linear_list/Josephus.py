# Josephus问题：n个人，从第k个人开始数，数到第m个出局（包括第k个人），空位跳过


from python语言描述.ch3_linear_list.single_circle_list import LCList


# 基于数组
def josephus(n, k, m):
    people = list(range(1, n + 1))

    i = k - 1
    for num in range(n):
        count = 0
        while count < m:
            if people[i] > 0:
                count += 1

            if count == m:
                print(people[i])
                people[i] = 0
            i = (i + 1) % n
    return


# 基于顺序表，复杂度 n2
def josephus_L(n, k, m):
    people = list(range(1, n + 1))
    i = k - 1

    for num in range(n, 0, -1):
        i = (i + m - 1) % num
        print(people.pop(i))


# 基于循环单链表，复杂度 mn
class Josephus(LCList):
    def turn(self, m):
        for i in range(m):
            self._rear = self._rear.next

    def __init__(self, n, k, m):
        LCList.__init__(self)
        for i in range(1, n+1):
            self.append(i)

        self.turn(k-1)
        while not self.is_empty():
            self.turn(m-1)
            print(self.pop())           # 比顺序表快在表头删除是 O（1）的复杂度


if __name__ == "__main__":
    print("first")
    josephus(10, 2, 2)
    print('tow')
    josephus_L(11, 5, 2)
    print('three')
    Josephus(8, 5, 8)
