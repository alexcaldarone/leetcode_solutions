"""
Suppose you are at a party with n people labeled from 0 to n - 1 and among them, there may exist one celebrity.
The definition of a celebrity is that all the other n - 1 people know the celebrity, but the celebrity does not know any of them.
Now you want to find out who the celebrity is or verify that there is not one. 
You are only allowed to ask questions like: "Hi, A. Do you know B?" to get information about whether A knows B. 
You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).
You are given an integer n and a helper function bool knows(a, b) that tells you whether a knows b. 
Implement a function int findCelebrity(n). There will be exactly one celebrity if they are at the party.
Return the celebrity's label if there is a celebrity at the party. If there is no celebrity, return -1.
Note that the n x n 2D array graph given as input is not directly available to you, 
and instead only accessible through the helper function knows. graph[i][j] == 1 represents person i knows person j, 
wherease graph[i][j] == 0 represents person j does not know person i.

Example 1:
    Input: graph = [[1,1,0],[0,1,0],[1,1,1]]
    Output: 1
    Explanation: There are three persons labeled with 0, 1 and 2. graph[i][j] = 1 means person i knows person j, otherwise graph[i][j] = 0 means person i does not know person j. The celebrity is the person labeled as 1 because both 0 and 2 know him but 1 does not know anybody.

Example 2:
    Input: graph = [[1,0,1],[1,1,0],[0,1,1]]
    Output: -1
    Explanation: There is no celebrity.
"""

# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0
        for i in range(n):
            if knows(candidate, i):
                candidate = i
        
        # check that the candidate doesnt know anyone
        for i in range(n):
            if i != candidate:
                if knows(candidate, i) or not knows(i, candidate):
                    return -1
        
        return candidate

# slow solution
class Solution2:
    def findCelebrity(self, n: int) -> int:
        g = [[0] * n for _ in range(n)]
        # g[i,j] = i knows j

        for i in range(n):
            for j in range(n):
                if i == j:
                    g[i][i] = 0
                else:
                    g[i][j] = int(knows(i, j))
        
        # celebrity: no outward edges, everybody knows him
        row_sums = []
        for i in range(n):
            row_sums.append(sum(g[i]))
        
        col_sums = []
        for i in range(n):
            col = 0
            for j in range(n):
                col += g[j][i]
            col_sums.append(col)
        
        print(row_sums, col_sums)

        celebs = 0
        res = 0
        for idx, (r, c) in enumerate(zip(row_sums, col_sums)):
            if r == 0 and c == n-1:
                celebs += 1
                res = idx
                break
        return res if celebs != 0 else -1
