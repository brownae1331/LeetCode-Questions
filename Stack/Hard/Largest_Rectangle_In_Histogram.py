def largestRectangleArea(heights: list[int]) -> int:
    stack = []
    max_area = 0
    for i in range(0, len(heights)):
        start = i
        while stack and stack[-1][1] > heights[i]:
            index, height = stack.pop()
            max_area = max((i - index) * height, max_area)
            start = index
        stack.append((start, heights[i]))

    for i, h in stack:
        max_area = max(h * (len(heights) - i), max_area)
    return max_area

if __name__ == "__main__":
    output = largestRectangleArea([2,1,5,6,2,3])
    print(output)