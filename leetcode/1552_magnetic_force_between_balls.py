"""
In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in his new invented basket. 
Rick has n empty baskets, the ith basket is at position[i], Morty has m balls and needs to distribute the balls into the baskets such that 
the minimum magnetic force between any two balls is maximum.
Rick stated that magnetic force between two different balls at positions x and y is |x - y|.
Given the integer array position and the integer m. Return the required force.

Example 1:
    Input: position = [1,2,3,4,7], m = 3
    Output: 3
    Explanation: Distributing the 3 balls into baskets 1, 4 and 7 will make the magnetic force between ball pairs [3, 3, 6]. 
    The minimum magnetic force is 3. We cannot achieve a larger minimum magnetic force than 3.

Example 2:
    Input: position = [5,4,3,2,1,1000000000], m = 2
    Output: 999999999
    Explanation: We can use baskets 1 and 1000000000.
"""

import math
from typing import List

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        res = 0
        n = len(position)
        l, h = 0, math.ceil(position[-1]/(m-1))

        while l <= h:
            mid = l + (h-l)//2
            if self.canPlaceBalls(mid, m, position):
                res = mid
                l = mid + 1
            else:
                h = mid - 1
        
        return res

    def canPlaceBalls(self, gap: int, m: int, position: List[int]) -> bool:
        prev_ball_pos = position[0]
        balls_placed = 1
        
        for i in range(1, len(position)):
            if position[i] - prev_ball_pos >= gap:
                prev_ball_pos = position[i]
                balls_placed += 1
            if balls_placed == m:
                return True
        
        return False