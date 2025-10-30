"""
Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

Example 1:
    Input: arr = [5,5,4], k = 1
    Output: 1
    Explanation: Remove the single 4, only 5 is left.

Example 2:
    Input: arr = [4,3,1,1,3,3,2], k = 3
    Output: 2
    Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.
"""

import heapq
from collections import defaultdict
from typing import List

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # count integers and their frequency
        # starting from the least frequent integers, remove them k times
        # return the unique number of integers left
        counts = defaultdict(int)

        for num in arr: 
            counts[num] += 1
        
        # store the frequencies and the numbers in a list
        heap = [(freq, num) for num, freq in counts.items()]

        heapq.heapify(heap)

        for _ in range(k):
            curr_freq, curr_num = heapq.heappop(heap)
            curr_freq -= 1
            if curr_freq > 0:
                heapq.heappush(heap, (curr_freq, curr_num))
        
        return len(heap)