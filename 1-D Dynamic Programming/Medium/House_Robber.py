def rob(nums: list[int]) -> int:
    rob1, rob2 = 0, 0

    for n in nums:
        rob1, rob2 = rob2, max(rob2, n + rob1)
    return rob2

if __name__ == "__main__":
    print(rob([1, 1, 3, 3]))