"""
A phrase is a palindrome if, after converting all uppercase letters into
lowercase letters and removing all non-alphanumeric characters, it reads
the same forward and backward. Alphanumeric characters include letters
and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""

        for ch in list(s):
            if ch.isalnum():
                if ch.isupper():
                    ch = ch.lower()
                newStr += ch

        reverseStr = newStr[::-1]
        return reverseStr == newStr


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
# "amanaplanacanalpanama" is a palindrome.
