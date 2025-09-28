"""
There are n pieces arranged in a line, and each piece is colored either by 'A' or by 'B'. 
You are given a string colors of length n where colors[i] is the color of the ith piece.
Alice and Bob are playing a game where they take alternating turns removing pieces from the line. In this game, Alice moves first.
Alice is only allowed to remove a piece colored 'A' if both its neighbors are also colored 'A'. She is not allowed to remove pieces that are colored 'B'.
Bob is only allowed to remove a piece colored 'B' if both its neighbors are also colored 'B'. He is not allowed to remove pieces that are colored 'A'.
Alice and Bob cannot remove pieces from the edge of the line.
If a player cannot make a move on their turn, that player loses and the other player wins.
Assuming Alice and Bob play optimally, return true if Alice wins, or return false if Bob wins.

Example 1:
    Input: colors = "AAABABB"
    Output: true
    Explanation:
    AAABABB -> AABABB
    Alice moves first.
    She removes the second 'A' from the left since that is the only 'A' whose neighbors are both 'A'.
    Now it's Bob's turn.
    Bob cannot make a move on his turn since there are no 'B's whose neighbors are both 'B'.
    Thus, Alice wins, so return true.

Example 2:
    Input: colors = "AA"
    Output: false
    Explanation:
    Alice has her turn first.
    There are only two 'A's and both are on the edge of the line, so she cannot move on her turn.
    Thus, Bob wins, so return false.

Example 3:
    Input: colors = "ABBBBBBBAAA"
    Output: false
    Explanation:
    ABBBBBBAAA -> ABBBBBBBAA
    Alice moves first.
    Her only option is to remove the second to last 'A' from the right.
    ABBBBBBBAA -> ABBBBBBAA
    Next is Bob's turn.
    He has many options for which 'B' piece to remove. He can pick any.
    On Alice's second turn, she has no more pieces that she can remove.
    Thus, Bob wins, so return false.
"""

# my initial solution
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        if len(colors) <= 2:
            return False
        
        l, r = 0, 1
        # i want the number of strings of length at least 3
        # and their length
        a = 0
        run_len = 1
        while r < len(colors):
            while r < len(colors) and colors[l] == colors[r] == "A":
                r += 1
                run_len += 1
            
            if run_len >= 3:
                a += run_len-2
            l, r = r, r+1
            run_len = 1

        b = 0
        l, r = 0, 1
        run_len = 1
        while r < len(colors):
            while r < len(colors) and colors[l] == colors[r] == "B":
                r += 1
                run_len += 1
            
            if run_len >= 3:
                b += run_len-2
            l, r = r, r+1
            run_len = 1

        if a <= 2 and b > 2:
            return False
        if b <= 2 and a > 2:
            return True
        if a == b:
            return False
        return a >= b
    
# better solution
class Solution2:
    def winnerOfGame(self, colors: str) -> bool:
        if len(colors) <= 2:
            return False
        
        run_len = 1
        a = b = 0
        for i in range(1, len(colors)):
            if colors[i] == colors[i-1]:
                run_len += 1
            else:
                if run_len >= 3:
                    if colors[i-1] == "A":
                        a += run_len-2
                    else:
                        b += run_len-2
                run_len = 1
        
        # last run at end of string
        if run_len >= 3:
            if colors[-1] == "A":
                a += run_len-2
            else:
                b += run_len-2
        return a > b