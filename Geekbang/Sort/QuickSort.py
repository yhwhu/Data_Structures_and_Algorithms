# 快速排序
# 以数据为中心，随机选择一个数据作为中间点，分区过程中进行了排序。
# 原地排序，但是不稳定


def quick_sort(lst):
    n = len(lst)
    return quick_sort_recursion(lst, 0, n)


def quick_sort_recursion(lst, start, end):
    if start >= end - 1:
        return

    mid = partition(lst, start, end)
    quick_sort_recursion(lst, start, mid)
    quick_sort_recursion(lst, mid, end)


def partition(lst, start, end):      # 数据交换导致不稳定
    i = start
    value = lst[end-1]
    for j in range(start, end):      # 巧妙的实现了原地分区
        if lst[j] < value:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1

    lst[end-1] = lst[i]
    lst[i] = value
    return i


if __name__ == "__main__":
    lst = [4,3,2,1,7,6,5]
    quick_sort(lst)         # 原地排序
    print("res:", lst)
