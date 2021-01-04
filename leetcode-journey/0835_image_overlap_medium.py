from collections import Counter
from typing import List


class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        ones_a, ones_b = [], []
        for i, row in enumerate(A):
            for j, cell in enumerate(row):
                if cell:
                    ones_a.append((i, j))
        for i, row in enumerate(B):
            for j, cell in enumerate(row):
                if cell:
                    ones_b.append((i, j))

        counter = Counter()
        for r1, c1 in ones_a:
            for r2, c2 in ones_b:
                counter[(r1 - r2, c1 - c2)] += 1
        return max(counter.values() or [0])


A = [[1,1,0],[0,1,0],[0,1,0]]
B = [[0,0,0],[0,1,1],[0,0,1]]
print(Solution().largestOverlap(A, B))