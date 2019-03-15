# 冒泡排序
# 以数字位置为中心，向后循环交换数字，即每次排好一个大的数据
# 没有数据交换时可以提前结束


def bubble_sort(lst):
    n = len(lst)
    if n <= 1:
        return lst

    for i in range(n-1):
        is_change = False
        for j in range(n-1-i):
            if lst[j] > lst[j+1]:
                tmp = lst[j]
                lst[j] = lst[j+1]   # 交换数据
                lst[j+1] = tmp
                is_change = True

        if not is_change:
            break

    return lst


if __name__ == "__main__":
    lst = [1000,5,2,10,7,7]   # 是稳定排序
    res = bubble_sort(lst)
    print(res)

    lst = [2,1,5,4,5,10,9,1]
    res = bubble_sort(lst)
    print("res", res)
