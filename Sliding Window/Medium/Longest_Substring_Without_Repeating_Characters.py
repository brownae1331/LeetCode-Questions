"""
Question:
        Given a string s, find the length of the longest substring without duplicate characters.

        A substring is a contiguous sequence of characters within a string.
"""


def lengthOfLongestSubstring(s: str) -> int:
    charSet = set()
    l = 0
    res = 0

    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        res = max(res, r - l + 1)
    return res


if __name__ == "__main__":
    output = lengthOfLongestSubstring(s="zxyzxyz")
    print(output)