"""
You are given two integer arrays nums1 and nums2 both of the same length. 
The advantage of nums1 with respect to nums2 is the number of indices i for which nums1[i] > nums2[i].
Return any permutation of nums1 that maximizes its advantage with respect to nums2.

Example 1:
    Input: nums1 = [2,7,11,15], nums2 = [1,10,4,11]
    Output: [2,11,7,15]

Example 2:
    Input: nums1 = [12,24,8,32], nums2 = [13,25,32,11]
    Output: [24,32,8,12]
"""

from collections import defaultdict
from typing import List

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        sorted_nums1 = sorted(nums1)
        sorted_nums2 = sorted(nums2)

        assigned = defaultdict(list)
        remaining = []

        j = 0
        for i, n in enumerate(sorted_nums1):
            if n > sorted_nums2[j]:
                assigned[sorted_nums2[j]].append(n)
                j += 1
            else:
                remaining.append(n)
        
        return [assigned[num].pop() if assigned[num] else remaining.pop()
            for num in nums2]