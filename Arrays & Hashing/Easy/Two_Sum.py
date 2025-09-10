"""
Question:
        Given an array of integers nums and an integer target,
        return the indices i and j such that nums[i] + nums[j] == target and i != j.
"""


def twoSum(nums: list[int], target: int) -> list[int]:
    """
    Uses a dictionary to store numbers as keys and their indices as values while iterating through the list.
    For each number, it checks if 'target - nums[i]' has already been seen; if so, it returns the pair of indicies.
    Otherwise, it stores the currect number with its index in the dictionary.

    Time Complexity: O(n) - The program loops through the nums list once
    Space Complexity: O(n) - A dictionary is created and all the nums could be added to it.
    """
    seen = {}
    for i in range(len(nums)):
        if target - nums[i] in seen:
            return [seen[target - nums[i]], i]
        seen[nums[i]] = i
    return []

if __name__ == "__main__":
    output = twoSum(nums=[4,5,6], target=10)
    print(output)