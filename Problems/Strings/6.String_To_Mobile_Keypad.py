"""
    1   |   2   |   3   |
        | A B C | D E F |
_________________________
    4   |   5   |   6   |
 G H I  | J K L | M N O |
_________________________
    7   |   8   |   9   |
P Q R S | T U V |W X Y Z|
_________________________
    *   |   0   |   #   |
        |       |       |
_________________________

Input : GEEKSFORGEEKS
Output : 4333355777733366677743333557777
For obtaining a number, we need to press a
number corresponding to that character for
number of times equal to position of the
character. For example, for character C,
we press number 2 three times and accordingly.

Input : HELLO WORLD
Output : 4433555555666096667775553
"""


def convertStringToMobileKeypad(string: str) -> str:
    numberPosition = [
        "2",
        "22",
        "222",
        "3",
        "33",
        "333",
        "4",
        "44",
        "444",
        "5",
        "55",
        "555",
        "6",
        "66",
        "666",
        "7",
        "77",
        "777",
        "7777",
        "8",
        "88",
        "888",
        "9",
        "99",
        "999",
        "9999",
    ]

    nums = ""

    for char in string:
        if char == " ":
            nums += "0"
        else:
            arrPosition = ord(char) - ord("A")
            nums += numberPosition[arrPosition]

    return nums


print(convertStringToMobileKeypad("GEEKSFORGEEKS"))
print(convertStringToMobileKeypad("HELLO WORLD"))
