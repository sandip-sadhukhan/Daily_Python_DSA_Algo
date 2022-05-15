"""Maximum and Minimum Element in an Array."""

from typing import List, Tuple


def linearSearchTechnique(arr: List[int]) -> Tuple[int, int]:
    """Linear Search, Time Complexity - O(n),
    Space Complexity - O(1)
    """

    # check if the array is empty
    if len(arr) == 0:
        return (0, 0)

    # assign the first element as min and max
    arr_max: int = arr[0]
    arr_min: int = arr[0]

    # comparing from 2nd element of array
    for element in arr[1:]:
        if element > arr_max:
            arr_max = element
        if element < arr_min:
            arr_min = element

    return (arr_max, arr_min)


def tournamentTechnique(
    arr: List[int], low: int, high: int
) -> Tuple[int, int]:
    """Tournament Technique,
    Time Complexity - O(n),
    Space Complexity - O(log(n))"""

    # checking if the arr is empty
    if len(arr) == 0:
        return (0, 0)  # indicate that arr is empty

    arr_max: int = arr[low]
    arr_min: int = arr[low]

    # if only one element is there
    if low == high:
        return (arr_max, arr_min)

    # if two element in array
    elif high == low + 1:
        if arr[low] > arr[high]:
            arr_max = arr[low]
            arr_min = arr[high]
        else:
            arr_max = arr[high]
            arr_min = arr[low]
        return (arr_max, arr_min)

    # more than 2 element
    else:
        mid: int = (low + high) // 2
        arr_max1, arr_min1 = tournamentTechnique(arr, low, mid)
        arr_max2, arr_min2 = tournamentTechnique(arr, mid + 1, high)

        return (max(arr_max1, arr_max2), min(arr_min1, arr_min2))


testCaseArr = [2220, 34, 22, 354, 32, 3, 444, 2, 22, 4]

result1 = linearSearchTechnique(testCaseArr)
print(f"Linear Search, max: {result1[0]}, min: {result1[1]}")

result2 = tournamentTechnique(testCaseArr, 0, len(testCaseArr) - 1)
print(f"Linear Search, max: {result2[0]}, min: {result2[1]}")
