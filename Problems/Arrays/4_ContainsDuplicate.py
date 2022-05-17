"""
Given an integer array nums, 
return true if any value appears at least twice
in the array, and return false if every element is distinct.
"""

from typing import List, Set


def containsDuplicate(nums: List[int]) -> bool:
    hashSet: Set[int] = set()

    for num in nums:
        if num in hashSet:
            return True
        else:
            hashSet.add(num)

    return False


print(containsDuplicate([1, 2, 3, 1]))
print(containsDuplicate([1, 2, 3, 4]))
