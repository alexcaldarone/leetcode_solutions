"""
An integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.
Given an integer n, return the largest number that is less than or equal to n with monotone increasing digits.

Example 1:
    Input: n = 10
    Output: 9

Example 2:
    Input: n = 1234
    Output: 1234

Example 3:
    Input: n = 332
    Output: 299
"""

from math import log10, floor

class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        if n == 0:
            return n

        def is_monotone(num, n_digits):
            for i in range(n_digits, -1, -1):
                s = num // 10**i
                if s > (num - s*10**(i)) // 10**(i-1) and i != 0:
                    return False
                num -= s*10**i
            return True
        
        i = 0
        n_digits = int(floor(log10(n)))
        
        for j in range(n_digits+1):
            # i want the closest number that ends in 9 smaller than n
            if is_monotone(n, n_digits):
                return n
            else:
                n = n - ((n % 10**j)+1)

        return n
