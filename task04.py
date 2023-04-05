"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List
def Kortej(A: List[int],B: List[int],C: List[int],D: List[int],):
    '''

    :param A: array with data
    :param B: array with data
    :param C: array with data
    :param D: array with data
    :return: 2
    '''

    count = 0

    for i in A:
        for j in B:
            for k in C:
                for l in D:
                    if i + j + k + l == 0:
                        count += 1
                        '''через лист ебани'''
    return count
A = [-48, -1, 64]
B = [0, -34, 48]
C = [1, 48, 85]
D = [0, 100, 56]
Kortej(A,B,C,D)

