"""
You are given an array of intervals, where intervals[i] = [starti, endi] and each starti is unique.
The right interval for an interval i is an interval j such that startj >= endi and startj is minimized. Note that i may equal j.
Return an array of right interval indices for each interval i. If no right interval exists for interval i, then put -1 at index i.

Example 1:
    Input: intervals = [[1,2]]
    Output: [-1]
    Explanation: There is only one interval in the collection, so it outputs -1.

Example 2:
    Input: intervals = [[3,4],[2,3],[1,2]]
    Output: [-1,0,1]
    Explanation: There is no right interval for [3,4].
        The right interval for [2,3] is [3,4] since start0 = 3 is the smallest start that is >= end1 = 3.
        The right interval for [1,2] is [2,3] since start1 = 2 is the smallest start that is >= end2 = 2.

Example 3:
    Input: intervals = [[1,4],[2,3],[3,4]]
    Output: [-1,2,-1]
    Explanation: There is no right interval for [1,4] and [3,4].
        The right interval for [2,3] is [3,4] since start2 = 3 is the smallest start that is >= end1 = 3.
"""

from typing import List, Tuple

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:

        def binary_search(lis: List[Tuple[int, int]], end: int):
            l, r = 0, len(lis)

            while l < r:
                mid = (l + r) // 2
                if lis[mid][0] < end:
                    l = mid + 1
                else:
                    r = mid
            
            if l == len(lis):
                return -1
            else:
                return l

        starts = [(s, i) for i, (s, e) in enumerate(intervals)]
        starts.sort(key=lambda x: x[0])
        
        res = []
        for i, (s, e) in enumerate(intervals):
            idx = binary_search(starts, e)
            res.append(idx if idx == -1 else starts[idx][1])
        
        return res