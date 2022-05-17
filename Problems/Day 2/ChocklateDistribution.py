from itertools import combinations
from typing import List


def simpleSolution(arr: List[int], m: int) -> int:
    """Time- O(nm) (not sure)
    Space - O(1)"""
    min_diff = int(1e9)

    all_comb = list(combinations(arr, m))
    # for each combination we wil find min, max, and diff
    for comb in all_comb:
        maxEle = max(comb)
        minEle = min(comb)
        diff = maxEle - minEle
        if diff < min_diff:
            min_diff = diff

    return min_diff


def efficientSolution(arr: List[int], m: int) -> int:
    """Time - O(nlogn)
    Space - O(n) for sorting array store"""

    newArr = arr.copy()
    newArr.sort()

    minDiff = newArr[-1] - newArr[0]

    for i in range(0, len(newArr) - m + 1):
        firstElement = newArr[i]
        lastElement = newArr[i + m - 1]
        diff = lastElement - firstElement
        if minDiff > diff:
            minDiff = diff

    return minDiff


print(simpleSolution([7, 3, 2, 4, 9, 12, 56], 3))  # 2
print(efficientSolution([3, 4, 1, 9, 56, 7, 9, 12], 5))  # 6
