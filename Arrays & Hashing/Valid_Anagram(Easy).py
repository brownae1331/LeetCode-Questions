"""
Question:
        Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

        An anagram is a string that contains the exact same characters as another string,
        but the order of the characters can be different.
"""


def isAnagram(s: str, t: str):
    """
    First compares the lengths of the strings since anagrams must be the same length.
    It then uses 2 dictionaries to count how many times each character appears in both strings.
    Compares the dictionaries; if they are equal, the strings are anagrams.

    Time Complexity: O(n) - The program iterates through the number of characters which takes O(n);
                            comparing the dictionaries also takes O(n), so total time complexity is O(n) + O(n) = O(n).
    Space Complexity: O(1) - The program creates two dictionaries, but each can store at most 26 possible characters, O(1) each.
    """
    count_s, count_t = {}, {}
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        count_s[s[i]] = 1 + count_s.get(s[i], 0)
        count_t[t[i]] = 1 + count_t.get(t[i], 0)
    return count_s == count_t


if __name__ == "__main__":
    output = isAnagram(s="jar", t="jam")
    print(output)