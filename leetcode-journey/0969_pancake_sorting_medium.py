class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        res, n = [], len(A)
        for i in range(n, 0, -1):
            pos = A.index(i)
            if pos == i - 1:
                continue
            if pos != 0:
                res.append(pos + 1)
                A[:pos + 1] = A[:pos + 1][::-1]
            res.append(i)
            A[:i] = A[:i][::-1]
        return res
