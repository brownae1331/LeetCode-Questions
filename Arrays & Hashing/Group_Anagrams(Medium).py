"""
Question:
        Given an array of strings strs, group all anagrams together into sublists.
        You may return the output in any order.

        An anagram is a string that contains the exact same characters as another string,
        but the order of the characters can be different.
"""

from collections import defaultdict


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    """
    Uses a dictionary where each key represents the character frequency of a word (stored as a 26-length tuple from letters a to z).
    Each value of the dictionary is a list so when iterating through the string, they can get appended to the correspoing key.

    Time Complexity: O(n * k) - n is the number of words in strs, and k is the maxiumum length of a word; there is a nested loop.
    Space Complexity: O(n * k) - the dictionary stores up to n keys, the values are lists containing all words; maximum length of a word is k.
    """
    anagram_dict = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord("a")] += 1
        anagram_dict[tuple(count)].append(s)
    return list(anagram_dict.values())

if __name__ == "__main__":
    output = groupAnagrams(strs=["act", "pots", "tops", "cat", "stop", "hat"])
    print(output)