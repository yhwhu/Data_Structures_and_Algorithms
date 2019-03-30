# 朴素串匹配算法：每次失败目标串前进一格
# t:目标串，p：模式串


def naive_matching(t, p):
    n = len(t)
    m = len(p)
    i, j = 0, 0

    while i < m and j < n:
        if p[i] == t[j]:
            i, j = i+1, j+1
        else:
            i, j = 0, j-i+1      # j会回溯

    if i == m:
        return j - i
    return -1


if __name__ == "__main__":
    t = 'abcdefg'
    p = 'ef'
    print(naive_matching(t, p))
