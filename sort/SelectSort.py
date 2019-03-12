# 选择排序
# 以数据为主，每次选择最小的数据放前面


def select_sort(lst):
    n = len(lst)
    if n <= 1:
        return lst

    for i in range(n-1):
        k = i
        for j in range(i, n, 1):
            if lst[k] > lst[j]:    # 查找最小的数据索引
                k = j
        tmp = lst[i]
        lst[i] = lst[k]            # 交换数据
        lst[k] = tmp
    return lst


if __name__ == "__main__":
    lst = [1000, 5, 2, 10, 7, 7]
    res = select_sort(lst)
    print(res)

    lst = [2,1,5,4,5,10,9,1]   # 不是稳定排序
    res = select_sort(lst)
    print(res)
