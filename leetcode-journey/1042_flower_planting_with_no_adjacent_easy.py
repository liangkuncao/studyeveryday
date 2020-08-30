from typing import List
from collections import defaultdict


class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        flowers = [0] * (N + 1)
        garden = defaultdict(list)
        for src, dst in paths:
            garden[src].append(dst)
            garden[dst].append(src)
        for i in range(1, N + 1):
            colors = set(range(1, 5))
            for neigh in garden[i]:
                if flowers[neigh] in colors:
                    colors.remove(flowers[neigh])
            flowers[i] = colors.pop()
        return flowers[1:]


print(Solution().gardenNoAdj(3, [[1,2],[2,3],[3,1]]))