"""
Question: 
        Given an integer array nums, return true if any value appears more than once in the array,
        otherwise return false.
"""


def hasDuplicate(nums: list[int]) -> bool:
    """
    A set is used which automatically remove duplicates when elements are added.
    If the set ends up smaller than the original list, it means some nubers apeared more than once.
    Therefore the function return True; otherwise, it returns False.
    
    Time complexity: O(n) - The program loops through the nums list once.
    Space complexity: O(n) - A set is created and all nums could be added to it.
    """
    nums_set = set()
    for num in nums:
        nums_set.add(num)
    return len(nums_set) != len(nums)


if __name__ == "__main__":
    output = hasDuplicate(nums=[1, 2, 3, 4])
    print(output)