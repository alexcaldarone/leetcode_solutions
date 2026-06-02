"""
There are n people, each person has a unique id between 0 and n-1. 
Given the arrays watchedVideos and friends, where watchedVideos[i] and friends[i] contain the list of watched videos and the list of friends respectively for the person with id = i.
Level 1 of videos are all watched videos by your friends, level 2 of videos are all watched videos by the friends of your friends and so on. 
In general, the level k of videos are all watched videos by people with the shortest path exactly equal to k with you. Given your id and the level of videos, 
return the list of videos ordered by their frequencies (increasing). For videos with the same frequency order them alphabetically from least to greatest. 

Example 1:
    Input: watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 1
    Output: ["B","C"] 
    Explanation: 
        You have id = 0 (green color in the figure) and your friends are (yellow color in the figure):
        Person with id = 1 -> watchedVideos = ["C"] 
        Person with id = 2 -> watchedVideos = ["B","C"] 
        The frequencies of watchedVideos by your friends are: 
            B -> 1 
            C -> 2

Example 2:
    Input: watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 2
    Output: ["D"]
    Explanation: 
        You have id = 0 (green color in the figure) and the only friend of your friends is the person with id = 3 (yellow color in the figure).
"""

from collections import defaultdict
from typing import List

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        # bfs to find people at distance k
        arr = [(id, friends[id], 0)]
        visited = set()
        visited.add(id)
        level_k_people = []
        while arr:
            node, neigs, dist = arr.pop(0)
            if dist == level:
                level_k_people.append(node)
                continue
            for neig in neigs:
                if neig not in visited:
                    visited.add(neig)
                    arr.append((neig, friends[neig], dist+1))
        
        video_freqs = defaultdict(int)
        for i in level_k_people:
            for video in watchedVideos[i]:
                video_freqs[video] += 1

        res = sorted(video_freqs, key=lambda x:(video_freqs[x], x))
        return res  