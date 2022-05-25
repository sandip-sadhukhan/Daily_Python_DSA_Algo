from typing import Optional

"""
Given a string S delete the characters which are appearing more
than once consecutively.
"""


class Solution:
    def removeConsecutiveCharacter(self, s: str) -> str:
        lastUsed: Optional[str] = None
        result: str = ""

        for char in s:
            if char == lastUsed:
                continue
            lastUsed = char
            result += char

        return result


# Test Cases
sol = Solution()
testCases = ["aabb", "aabaa", "aaab"]

for testCase in testCases:
    print(f"{testCase} - {sol.removeConsecutiveCharacter(testCase)}")
