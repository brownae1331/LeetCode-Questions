"""
Question:
        Given an integer array nums, return all the triples [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0,
        and the indicies i, j and k are distinct.

        The output should not contain any duplicate triplets. You may return the output and the triplets in any order.
"""


def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort() #[-4, -1, -1, 0, 1, 2]
    res = []

    for i in range(len(nums)):
        if nums[i] == nums[i-1]:
            continue

        l, r = i+1, len(nums)-1
        while l < r:
            threeSum = nums[i] + nums[l] + nums[r]
            if threeSum < 0:
                l += 1
            elif threeSum > 0:
                r -= 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l-1] and l < r:
                    l += 1
    return res


if __name__ == "__main__":
    output = threeSum(nums=[-1, 0, 1, 2, -1, -4])
    print(output)