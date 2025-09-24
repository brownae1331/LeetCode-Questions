"""
Question:
        You are given a string s consisting of only uppercase english characters and an integer k.
        You can choose up to k characters of the string and replace them with any other uppercase English character.

        After performing at most k replacements, return the length of the longest substring which contains only on distinct character.
"""


def characterReplacement(s: str, k: int) -> int:
    l = 0
    res = 0
    count = {}
    maxChr = 0

    for r in range(len(s)):
        count[s[r]] = count.get(s[r], 0) + 1
        maxChr = max(maxChr, count[s[r]])

        while r - l + 1 - maxChr > k:
            count[s[l]] -= 1
            l += 1
        res = max(res, r - l + 1)
    return res

if __name__ == "__main__":
    output = characterReplacement(s="AAABABB", k=1)
    print(output)