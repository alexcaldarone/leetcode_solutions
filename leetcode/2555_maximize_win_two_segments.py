"""

"""

from typing import List

class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        l = 0
        res = 0
        dp = [0] * len(prizePositions)
        for r in range(len(prizePositions)):
            while prizePositions[r] - prizePositions[l] > k:
                l += 1
            
            dp[r] = max((dp[r-1] if r > 0 else 0), r-l+1)
            res = max(res, r-l+1+(dp[l-1] if l > 0 else 0))        
        
        return res