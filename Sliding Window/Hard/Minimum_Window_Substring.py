"""
Question:
        Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates,
        is present in the substring. If such a substring does not exists, return an empty string "".
"""

def minWindow(s: str, t: str) -> str:
    tCount = {}
    for c in t:
        tCount[c] = tCount.get(c, 0) + 1

    res = ""
    for l in range(len(s)):
        substring = ""
        ssCount = {}
        r = l
        if tCount.get(s[l], 0) > 0:
            substring += s[l]
            ssCount[s[l]] = ssCount.get(s[l], 0) + 1

            while r < len(s) - 1 and tCount != ssCount:
                r += 1
                if tCount.get(s[r], 0) > 0:
                    ssCount[s[r]] = ssCount.get(s[r], 0) + 1
                substring += s[r]
            
            equal = True
            for key, value in tCount.items():
                if ssCount.get(key, 0) < value:
                    equal = False

            if equal and (not res or len(res) > len(substring)):
                res = substring
    return res


def betterMinWindow(s: str, t: str) -> str:
    tCount, windowCount = {}, {}
    for c in t:
        tCount[c] = tCount.get(c, 0) + 1

    l = 0
    res = ""
    have, need = 0, len(tCount)
    for r in range(len(s)):
        windowCount[s[r]] = windowCount.get(s[r], 0) + 1
        if s[r] in tCount and windowCount[s[r]] == tCount.get(s[r], 0):
            have += 1
        
        while have == need:
            if not res or r-l+1 < len(res):
                res = s[l:r+1]

            windowCount[s[l]] -= 1
            if s[l] in tCount and windowCount[s[l]] < tCount[s[l]]:
                have -= 1
            l += 1 
    return res


if __name__ == "__main__":
    output = betterMinWindow(s="aa", t="aa")
    print(output)