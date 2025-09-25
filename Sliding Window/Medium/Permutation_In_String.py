"""
Question:
        You are given two strings s1 and s2.

        Return true if s2 contains a permutation of s1, or false otherwise. 
        That meanse if a permutation of s1 exists as a substring of s2, then return true

        Both strings only contain lowercase letters.
"""

def checkInclusion(s1: str, s2: str) -> bool:
    s1Count = [0] * 26
    for c in s1:
        s1Count[ord(c) - ord("a")] += 1
    
    l = 0
    ssCount = [0] * 26
    for r in range(len(s2)):
        ssCount[ord(s2[r]) - ord("a")] += 1

        if r - l + 1 < len(s1):
            continue

        if ssCount != s1Count:
            ssCount[ord(s2[l]) - ord("a")] -= 1
            l += 1
        else:
            return True
    return False

if __name__ == "__main__":
    output = checkInclusion(s1="abc", s2="lecabee")
    print(output)