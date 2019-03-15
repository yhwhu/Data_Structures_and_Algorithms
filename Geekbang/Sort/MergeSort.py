# 归并排序
# 以位置为中心，左右划分等分区间
# 归：每次从中间划分为两个小区间，直到区间内都是1
# 并：将两个小区间合并为一个大区间，最多需要消耗o（n）的空间（中间合并占用空间可以释放）


def merge_sort(lst):
    n = len(lst)
    return merge_sort_recursion(lst, 0, n)


def merge_sort_recursion(lst, start, end):  # 左闭右开
    if start >= end - 1:
        return [lst[start]]

    mid = (start + end) // 2
    left = merge_sort_recursion(lst, start, mid)     # 归
    right = merge_sort_recursion(lst, mid, end)

    # merge left and right
    res = merge(left, right, start, mid, end)        # 并

    return res


def merge(left, right, start, mid, end):
    i = 0
    j = 0

    res_merge = []
    while i < (mid - start) and j < (end - mid):
        if left[i] <= right[j]:                  # 遇到相同数时，先插入前面的数字，保证时稳定排序
            res_merge.append(left[i])
            i += 1
        else:
            res_merge.append(right[j])
            j += 1

    if i < (mid - start):
        res_merge += left[i:]
    else:
        res_merge += right[j:]

    return res_merge


if __name__ == "__main__":
    lst = [5, 4, 3, 1, 9, 6, -1]
    res = merge_sort(lst)
    print("res", res)
