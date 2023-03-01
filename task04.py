"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
рорююрпг
"""
def Kortej():
    A = [-48, -1, 64]
    B = [0, -34, 48]
    C = [1, 48, 85]
    D = [0, 100, 56]
    count = 0

    for i in A:
        for j in B:
            for k in C:
                for l in D:
                    if i + j + k + l == 0:
                        count += 1
    return count
Kortej()

