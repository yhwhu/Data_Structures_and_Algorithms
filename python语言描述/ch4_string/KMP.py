# 无回溯串匹配算法（KMP算法）


def matching_KMP(t, p, pnext):
    """KMP串匹配，主函数"""

    j, i = 0, 0
    n, m = len(t), len(p)
    while j < n and i < m:
        if p[i] == t[j] or i == -1:  # i==-1,说明没有任何信息可以利用，下一步j+1，i=0
            i, j = i+1, j+1
        else:
            i = pnext[i]
    if i == m:
        return j - i
    return -1


def gen_next(p):
    """生成针对p中各位置i的下一检查位置表，用于KMP算法"""

    i, k, m = 0, -1, len(p)
    pnext = [-1] * m
    while i < m-1:
        if p[i] == p[k] or k == -1:
            i, k = i+1, k+1
            if p[i] == p[k]:   # pi与tj不等，推出pk也与tj不等
                pnext[i] = pnext[k]     # 前移变快
            else:
                pnext[i] = k
        else:
            k = pnext[k]
    return pnext


if __name__ == "__main__":
    t = 'abcdefefdafefgefgdafefcefdafefc'
    p = 'efdafefc'
    pnext = gen_next(p)
    print(pnext)
    print(matching_KMP(t, p, pnext))
