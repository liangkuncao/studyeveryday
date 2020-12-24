class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        res = 0
        ct = defaultdict(int)
        for a in A:
            for b in B:
                ct[a + b] += 1
        for c in C:
            for d in D:
                if -(c + d) in ct:
                    res += ct[-(c + d)]
        return res