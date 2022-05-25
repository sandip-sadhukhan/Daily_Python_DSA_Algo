from typing import Dict, List

"""
Write a function to find the longest common prefix string
amongst an array of strings.

If there is no common prefix, return an empty string "".

I will use trie.
"""


# Normal Solution
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        maxPrefix: str = ""
        minLength: int = min([len(string) for string in strs])

        for i in range(minLength):
            temp = strs[0][i]

            for string in strs[1:]:
                if string[i] != temp:
                    return maxPrefix

            maxPrefix += temp

        return maxPrefix


# Trie Solution
class TrieNode:
    def __init__(self):
        self.children: Dict[str, "TrieNode"] = {}
        self.endOfWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root

        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]

        return True


class TrieSolution:
    def longestCommonPrefixWithTrie(self, strs: List[str]) -> str:
        if strs is None or len(strs) == 0:
            return ""

        if len(strs) == 1:
            return strs[0]

        trie = Trie()

        for string in strs:
            if not string:
                return ""
            trie.insert(string)

        # Find LCP
        curr: TrieNode = trie.root
        lcp: str = ""

        while True:
            if len(curr.children) != 1:
                break
            children_key = list(curr.children.keys())[0]
            children = list(curr.children.values())[0]
            lcp += children_key
            if children.endOfWord:
                break
            curr = children

        return lcp


# Test cases
testCases = [["ab", "a"]]

print("Normal Solution")
print("=================")
sol = Solution()
for testCase in testCases:
    print(f"{testCase} - {sol.longestCommonPrefix(testCase)}")

print("Trie Solution")
print("=================")
trieSol = TrieSolution()
for testCase in testCases:
    print(f"{testCase} - {trieSol.longestCommonPrefixWithTrie(testCase)}")
