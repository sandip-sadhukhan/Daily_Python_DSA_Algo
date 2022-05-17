"""
Given an integer array nums, 
find the contiguous subarray 
(containing at least one number) 
which has the largest sum and return its sum.
"""

from typing import List


def kadaneAlgo(nums: List[int]) -> int:
    """Time - O(n), space - O(1)"""
    maxSum: int = int(-1e9)
    currSum: int = 0

    for num in nums:
        currSum += num
        if maxSum < currSum:
            maxSum = currSum

        if currSum < 0:
            currSum = 0

    return maxSum


print(kadaneAlgo([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
