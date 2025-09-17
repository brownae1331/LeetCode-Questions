"""
Question:
        You are given an integer array heights where heights[i] represents the height of the ith bar.

        You may choose any two bars to form a container. Return the maximum amount of water a container can store.
"""


def maxArea(heights: list[int]) -> int:
    l, r = 0, len(heights)-1
    bestArea = 0

    while l < r:
        area = (r - l) * min(heights[l], heights[r])
        bestArea = max(bestArea, area)

        if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1
    return bestArea

if __name__ == "__main__":
    output = maxArea(heights=[1, 7, 2, 5, 4, 7, 3, 6])
    print(output)