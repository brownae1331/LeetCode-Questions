"""
Question:
        Given a string s, return true if it is a plaindrome, otherwise retrun false.

        A palindrome is a string that reads the same forward and backwards. 
        It is also case-insensitive and ignores all non-alphanumeric characters

        Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).
"""

def isPalindromeReverseString(s: str) -> bool:
    newStr = "" 
    for c in s:
        if c.isalnum():
            newStr += c.lower()
    return newStr == newStr[::-1]


def isPalindromeTwoPointers(s: str) -> bool:
    l, r = 0, len(s) - 1

    while l < r:
        while l < r and not alphaNum(s[l]):
            l += 1
        while r > l and not alphaNum(s[r]):
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True

def alphaNum(c: str):
    return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))

if __name__ == "__main__":
    output = isPalindromeTwoPointers(s="Was it a car or a cat I saw?")
    print(output)