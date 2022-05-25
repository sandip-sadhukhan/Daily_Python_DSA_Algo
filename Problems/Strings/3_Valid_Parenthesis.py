from typing import List

"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']'
, determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack: List[str] = []

        for bracket in s:
            if bracket in ["(", "{", "["]:
                stack.append(bracket)
            elif len(stack) == 0:
                return False
            else:
                popElement = stack.pop()
                if bracket == ")" and popElement != "(":
                    return False
                if bracket == "}" and popElement != "{":
                    return False
                if bracket == "]" and popElement != "[":
                    return False

        return len(stack) == 0


# Test Cases
sol = Solution()
testCases = ["()", "(){}[]", "(]"]

for testCase in testCases:
    print(f"{testCase} - {sol.isValid(testCase)}")
