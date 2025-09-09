"""
Question:
        Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

        Each product is guaranteed to fit in a 32-bit integer.

        Follow-up: Could you solve it in O(n) time without using the division operation?
"""


def productExceptSelf(nums: list[int]) -> list[int]:
    res = [0] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]

    return res

if __name__ == "__main__":
    output = productExceptSelf(nums=[1,2,3,4])
    print(output)