"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. 
You can only see the k numbers in the window. Each time the sliding window moves right by one position.
Return the max sliding window.

Example 1:
    Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
    Output: [3,3,5,5,6,7]
    Explanation: 
    Window position                Max
    ---------------               -----
    [1  3  -1] -3  5  3  6  7       3
    1 [3  -1  -3] 5  3  6  7       3
    1  3 [-1  -3  5] 3  6  7       5
    1  3  -1 [-3  5  3] 6  7       5
    1  3  -1  -3 [5  3  6] 7       6
    1  3  -1  -3  5 [3  6  7]      7

Example 2:
    Input: nums = [1], k = 1
    Output: [1]
"""

from collections import deque
from typing import List

class Solution2:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # this solution here is correct but becomes inefficient for large k (O(n*k) time complexity)
        res = [max(nums[0:k])]
        queue = deque(nums[0:k])
        
        for i in range(k, len(nums)):
            queue.popleft()
            queue.append(nums[i])
            curr_max = float("-inf")
            for _ in range(k):
                curr = queue.popleft()
                curr_max = max(curr_max, curr)
                queue.append(curr)
            res.append(curr_max)
        
        return res

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        queue = deque()

        for i, num in enumerate(nums):
            while queue and nums[queue[-1]] <= num:
                queue.pop()
            queue.append(i)
            while queue[0] < i-k+1:
                queue.popleft()
            res.append(nums[queue[0]])
        
        return res[k-1:]