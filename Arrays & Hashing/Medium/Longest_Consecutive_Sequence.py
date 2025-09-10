"""
Question:
        Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

        A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. 
        The elements do not have to be consecutive in the original array.

        You must write an algorithm that runs in O(n) time.
"""


from collections import defaultdict


def longestConsecutive(nums: list[int]) -> int:
    """
    First the nums list is converted to a set to get rid of duplicates and to allow constant-time lookups.
    It then iterates through the set to check if it is the start of a sequence by check if num - 1 is not in the set.
    For each starting number, it counts how many consecutive numbers exist in the set, updating the maximum length so far.

    Time Complexity: O(n) - The sequence is only traversed once
    Space Complexity: O(n) - The set is created from the nums list
    """
    numsSet = set(nums)
    longest = 0
    
    for num in numsSet:
        if num-1 not in numsSet:
            length = 0
            while (num + length) in numsSet:
                length += 1
        longest = max(longest, length)
    return longest


if __name__ == "__main__":
    output = longestConsecutive(nums=[0,3,2,5,4,6,1,1])
    print(output)