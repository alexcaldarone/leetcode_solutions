"""
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

Example 1:
    Input: intervals = [[0,30],[5,10],[15,20]]
    Output: 2

Example 2:
    Input: intervals = [[7,10],[2,4]]
    Output: 1
"""

import heapq
from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        res = 0

        intervals.sort()
        print(intervals)
        heap = []

        for start, end in intervals:
            while heap and start >= heap[0]:
                heapq.heappop(heap) 
            
            heapq.heappush(heap, end)
            res = max(res, len(heap))

        return res