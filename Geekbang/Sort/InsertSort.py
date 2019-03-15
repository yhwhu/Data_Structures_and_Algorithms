# 插入排序
# 以数据为中心，每次将一个数据插入
# 1.数据插哪 2.数据搬移
# 要在循环内更改变量，事先必须先定义，参考k=0，栈的思想


def insert_sort(lst):
    n = len(lst)
    if n <= 1:
        return lst

    for i in range(1, n):
        value = lst[i]
        k = -1
        for j in range(i-1, -1, -1):
            k = j
            if lst[j] > value:
                lst[j+1] = lst[j]   # 数据搬移
            else:
                k += 1
                break
        lst[k] = value   # 数据插哪
    return lst


if __name__ == "__main__":
    lst = [1,3,2,4,8,6]           # 是稳定排序
    res = insert_sort(lst)
    print("res", res)

    lst = [2,1,5,4,5,10,9,1]
    res = insert_sort(lst)
    print("res", res)
