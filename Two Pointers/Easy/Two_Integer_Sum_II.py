"""
Question:
        Given an array of integers numbers that is sorted in non-decreasing order.

        Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target
        number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use
        the same element twice.

        There will always be exactly one valid solution

        Your solution must use O(1) additional space.
"""


def twoSum(numbers: list[int], target: int) -> list[int]:
    l, r = 1, len(numbers)
    while l < r:
        res = numbers[l-1] + numbers[r-1]
        if res < target:
            l += 1
        elif res > target:
            r -= 1
        else:
            return [l, r]
    return []

if __name__ == "__main__":
    output = twoSum(numbers=[1, 2, 3, 4], target=3)
    print(output)