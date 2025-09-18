"""
Question:
        You are given an array of non-negative integers height which represent an elevation map.
        Each value height[i] represents the height of a bar, which has a width of 1.

        Return the maximum area of water that can be trapped between the bars.
"""


def trapFirstTry(height: list[int]) -> int:
    totalArea = 0
    for i in range(len(height)):
        maxLeftHeight = 0
        maxRightHeight = 0

        for j in range(i, -1, -1):
            maxLeftHeight = max(maxLeftHeight, height[j])
        for k in range(i, len(height)):
            maxRightHeight = max(maxRightHeight, height[k])

        totalArea += 0 if min(maxLeftHeight, maxRightHeight) - height[i] < 0 else min(maxLeftHeight, maxRightHeight) - height[i]

    return totalArea


def trapPointers(height: list[int]) -> int:
    l, r = 0, len(height)-1
    totalArea = 0
    maxL, maxR = 0, 0
    while l < r:
        maxL = max(maxL, height[l])
        maxR = max(maxR, height[r])
        if maxL <= maxR:
            l += 1
            totalArea += 0 if maxL - height[l] < 0 else maxL - height[l]
        else:
            r -= 1
            totalArea += 0 if maxR - height[r] < 0 else maxR - height[r]
    return totalArea


if __name__ == "__main__":
    output = trapPointers(height=[0, 2, 0, 3, 1, 0, 1, 3, 2, 1])
    print(output)