class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pos = [0] * 1001
        for p, s, e in trips:
            pos[s] += p
            pos[e] -= p
        curr = 0
        for p in pos:
            curr += p
            if curr > capacity:
                return False
        return True