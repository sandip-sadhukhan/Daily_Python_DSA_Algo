"""
Write an efficient program to print all the duplicates
and their counts in the input string
"""


def printDuplicates(string: str):
    string = string.lower().replace(" ", "")
    TOTAL_CHARS = 26
    charsCount = [0] * TOTAL_CHARS

    for char in string:
        index = ord(char) - ord("a")
        charsCount[index] += 1

    for index, charCount in enumerate(charsCount):
        if charCount > 1:
            print(f"{chr(ord('a') + index)}, count = {charCount}")


testString = "test string"
printDuplicates(testString)
