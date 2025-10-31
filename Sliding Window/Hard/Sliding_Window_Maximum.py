import heapq
def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    heap, res = [], []
    l = 0
    for r in range(len(nums)):
        heapq.heappush(heap, (-nums[r], r))

        while heap[0][1] < l:
            heapq.heappop(heap)
        
        if r - l + 1 == k:
            res.append(-heap[0][0])
            l += 1
    return res

if __name__ == "__main__":
    output = maxSlidingWindow(nums=[1,2,1,0,4,2,6], k=3)
    print(output)