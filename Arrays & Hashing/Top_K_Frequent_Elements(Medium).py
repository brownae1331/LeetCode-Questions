"""
Question:
        Given an integer array nums and an integer k, return the k most frequent elements within the array.

        The test cases are generated such that the answer is always unique.

        You may return the output in any order.
"""

import heapq


def topKFrequentHeap(nums: list[int], k: int) -> list[int]:
    """
	The program first uses a dictionary that maps each number to how many times it appears.
    Then a min-heap is used to keep the smallest element at the top; the heap is ordered by the frequency of the numbers.
    When the heap gets bigger than k the program pops the smallest frequeny element.
    Then it iterates through the heap, appends the to a list and returns the list.
    
    Time Complexity: O(n * logk) - Iterates over nums once (n) to create the count_dict;
									There are m keys in count_dict where m <= n;
                                    Each heappop takes O(logk); so overall complexity is O(n + m * logk)
    Space Complexity: O(n + k) - Stores up to m unique elements in count_dict. Stores up to k elements in heap.
    """
    count_dict = {}
    for num in nums:
        count_dict[num] = count_dict.get(num, 0) + 1
    
    heap = []
    for num in count_dict.keys():
        heapq.heappush(heap, (count_dict[num], num))
        if len(heap) > k:
            heapq.heappop(heap)

    res = []
    for i in range(k):
        res.append(heapq.heappop(heap)[1])
    return res
    

def topKFrequentBucketSort(nums: list[int], k: int) -> list[int]:
    """
    The program first uses a dictionary that maps each number to how many times it appears.
    Then, it creates a list of buckets, where the index represent a frequency and each bucket stores the numbers that appear that many times.
    By iterating from the highest frequency downwards, it collects number into the result list until k elements are gathered.

    Time Complexity: O(n) - Iterates through nums once (n); filling the buckets iterates through at most m unique numbers. (m <= n).
                            Combined, this step is O(n + m); simplifies to O(n)
    Space Complexity: O(n) - Stores up to m unique numbers in count_dict; each number is stored once in one bucket; result list stores k numbers.
    """
    count_dict = {}
    freq =[[] for i in range(len(nums) + 1)]
    for num in nums:
        count_dict[num] = 1 + count_dict.get(num, 0)
    for num, cnt in count_dict.items():
        freq[cnt].append(num)
    
    res = []
    for i in range(len(freq) - 1, 0, -1):
        for num in freq[i]:
            res.append(num)
            if len(res) == k:
                return res

if __name__ == "__main__":
    output = topKFrequentBucketSort(nums=[1,2,2,3,3,3], k=2)
    print(output)