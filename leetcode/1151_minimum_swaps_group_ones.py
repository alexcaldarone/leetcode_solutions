"""
Given a binary array data, return the minimum number of swaps required to group all 1's present in the array together in any place in the array.

Example 1:
    Input: data = [1,0,1,0,1]
    Output: 1
    Explanation: 
        There are 3 ways to group all 1's together:
        [1,1,1,0,0] using 1 swap.
        [0,1,1,1,0] using 2 swaps.
        [0,0,1,1,1] using 1 swap.
        The minimum is 1.

Example 2:
    Input: data = [0,0,0,1,0]
    Output: 0
    Explanation: Since there is only one 1 in the array, no swaps are needed.

Example 3:
    Input: data = [1,0,1,0,1,0,0,1,1,0,1]
    Output: 3
    Explanation: One possible solution that uses 3 swaps is [0,0,0,0,0,1,1,1,1,1,1].
"""

from typing import List

class Solution:
    def minSwaps(self, data: List[int]) -> int:
        n = len(data)
        number_ones = sum(data)

        if number_ones <= 1:
            return 0

        swaps = number_ones - sum(data[:number_ones])
        prev_ones = sum(data[:number_ones])

        for i in range(1, n-number_ones+1):
            ones = (prev_ones + data[i+number_ones-1] - data[i-1])
            curr = number_ones - ones
            swaps = min(swaps, curr)
            prev_ones = ones

        return swaps