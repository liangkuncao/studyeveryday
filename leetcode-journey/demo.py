from typing import List

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        count1, count2 = [0] * 7, [0] * 7
        target = None
        for a, b in zip(A, B):
            count1[a] += 1
            count2[b] += 1
        for i in range(1, len(count1)):
            if count1[i] + count2[i] >= len(A):
                target = i
                break
        if not target:
            return -1
        both_count = 0
        for a, b in zip(A, B):
            if a != target and b != target:
                return -1
            if a == target and b == target:
                both_count += 1
        return min(count1[target] - both_count, count2[target] - both_count)


A = [2,1,2,4,2,2]
B = [5,2,6,2,3,2]
print(Solution().minDominoRotations(A, B))

C = [1,1,1,1,1,1,1,1]
D = [1,1,1,1,1,1,1,1]
print(Solution().minDominoRotations(C, D))
