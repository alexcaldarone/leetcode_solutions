"""
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
Given an integer n, return the nth ugly number.

Example 1:
    Input: n = 10
    Output: 12
    Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.

Example 2:
    Input: n = 1
    Output: 1
    Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
"""

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        uglies = [1]
        seen = set()
        indexes = [0] * 3
        for i in range(1, n):
            next_ugly_idx, next_ugly = -1, float("inf")
            for idx, mult in enumerate((2,3,5)):
                prod = mult * uglies[indexes[idx]]
                while prod in seen:
                    indexes[idx] += 1
                    prod = mult * uglies[indexes[idx]]
                if next_ugly > prod:
                    next_ugly = prod
                    next_ugly_idx = idx
            
            indexes[next_ugly_idx] += 1
            seen.add(next_ugly)
            uglies.append(next_ugly)
        
        return uglies[-1]