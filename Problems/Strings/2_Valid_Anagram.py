"""
Given two strings s and t, return true if t is an anagram of s,
and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters
of a different wordor phrase, typically using all the original
letters exactly once.
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        newList = list(s)

        if len(s) != len(t):
            return False

        for i in list(t):
            if i in newList:
                newList.remove(i)
            else:
                return False
        return True


print(Solution().isAnagram("rat", "cat"))
